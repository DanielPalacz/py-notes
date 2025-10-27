import socket
import threading
from sys import argv
import psutil
import logging
import enum

class HttpResponseMethod(enum.Enum):
    GET = 1
    POST = 2
    PUT = 3
    PATCH = 4
    DELETE = 5
    OPTIONS = 6

    @classmethod
    def get_all_members(cls):
        return list(map(lambda m: m.name, cls))


def configure_logger(logger_name: str) -> logging.Logger:
    """Configures logger.

    Uses env variable LOG_LEVEL_NAME:
     - CRITICAL = 50
     - FATAL = 50
     - ERROR = 40
     - WARNING = 30
     - INFO = 20
     - DEBUG = 10

    Args:
        logger_name: Logger name.

    Returns:
        Logger object.
    """
    log_level_matrix = {"CRITICAL": 50, "FATAL": 50, "ERROR": 40, "WARNING": 30, "INFO": 20, "DEBUG": 10}

    log_level_name = "DEBUG"
    log_level_value = log_level_matrix[log_level_name]

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level_value)
    logger_handler = logging.StreamHandler()
    # logger_handler = RotatingFileHandler(f"logs/{logger_name}.log", maxBytes=100 * 1024 * 1024, backupCount=20)
    logger_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    logger_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_handler)

    return logger

def release_process(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            pid = conn.pid
            if pid is None:
                print(f"Lack PID for connection: {conn}")
                return None
            try:
                proc = psutil.Process(pid)
                print(f"Found process {proc.pid} ({proc.name()}) listening on port {port}")
                print("Cmdline:", " ".join(proc.cmdline()))

                # Spróbuj zakończyć proces łagodnie
                proc.terminate()
                try:
                    proc.wait(timeout=3)
                    print(f"Process {pid} terminated gracefully.")
                except psutil.TimeoutExpired:
                    print(f"Process {pid} did not terminate, killing...")
                    proc.kill()
                    print(f"Process {pid} killed.")
            except psutil.NoSuchProcess:
                print(f"Process {pid} already gone.")

    return None


class HttpRequestParser:
    LOGGER = configure_logger("HttpRequestParser")

    def __init__(self, raw_data: bytes):
        self.raw_data = raw_data
        self.method = None
        self.path = None
        self.version = None
        self.headers = {}
        self.body = None
        self.valid = False

        try:
            self._parse()
            self.valid = True
        except Exception as e:
            self.LOGGER.error(f"[HttpRequestParser] Problems during http request parsing (details: {str(e)}).")
            self.valid = False

    def _parse(self):
        # Bytes to text.
        # (But HTTP accepts Latin-1? - > iso-8859-1)
        text = self.raw_data.decode("utf-8")

        # Headers, body - deduction / extraction:
        headers, body = text.split("\r\n\r\n", 1)

        # 1st line, Request Line:, method and url-path:
        headers_lines = headers.split("\r\n")
        request_line = headers_lines[0]
        self._parse_request_line(request_line)

        # Other headers:
        for line in headers_lines[1:]:
            if ":" not in line:
                raise ValueError(f"Incorrect HTTP header: {line}")

            name, value = line.split(":", 1)
            self.headers[name.strip()] = value.strip()

        self.body = body

    def _parse_request_line(self, line: str):
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f"Incorrect HTTP header ({line}).")

        self.method, self.path, self.version = parts

        # Basic validation:
        if self.version not in ("HTTP/1.0", "HTTP/1.1"):
            raise ValueError(f"Not supported HTTP version ({self.version}).")
        if not self.path.startswith("/"):
            raise ValueError(f"Incorrect path ({self.path}).")
        if self.method not in ("GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH"):
            raise ValueError("Unknown HTTP method ({self.method}).")
        if self.method not in ("GET",):
            raise ValueError(f"Method`s {self.method} support is not provided yet.")

    def __repr__(self):
        return (f"<HttpRequestParser method={self.method!r}, path={self.path!r}, "
                f"version={self.version!r}, valid={self.valid}>")


LOGGER = configure_logger("http_danserv")

# Configuration - server details
try:
    PORT = int(argv[1])
except IndexError:
    PORT = 9000

HOST = "127.0.0.1"
SERVER_ADDRESS = (HOST, PORT)


def make_response(url_path: str, is_favicon: bool = False, incorrect_request: bool = False, http_method: str = "GET") -> bytes:
    thread_name = threading.current_thread().name
    LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] "
                 f"trying to handle http request for {url_path!r} page response (http_method: {http_method}).")

    if http_method != "GET":
        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] "
                     f"http request is not GET-like, so returning 405 Error code (http_method: {http_method}).")
        resp_body = "Method Not Allowed.".encode()
        resp = b"HTTP/1.1 405 Method Not Allowed\r\n" \
               b"Content-Type: text/plain; charset=utf-8\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp

    if incorrect_request:
        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] "
                     f"http request doesnt have correct structure, so returning 400 Error code (http_method: {http_method}).")
        resp_body = "Bad request.".encode()
        resp = b"HTTP/1.1 400 Bad request\r\n" \
               b"Content-Type: text/plain; charset=utf-8\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp

    if is_favicon:
        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] "
                     f"http request is related to favicon picture, returning hardcoded favicon bytes (http_method: {http_method}).")
        resp_body_favicon = b'\x00\x00\x01\x00\x02\x00\x10\x10\x00\x00\x00\x00\x20\x00\x54\x02\x00\x00\x26\x00\x00\x00\x20\x20\x00\x00\x00\x00\x20\x00\x2a\x01\x00\x00\x7a\x02\x00\x00\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\x00\x00\x02\x1b\x49\x44\x41\x54\x78\x9c\x65\xd3\x3d\x88\x5c\x55\x18\x06\xe0\xe7\xcc\xbd\x77\xff\x64\x25\x89\x28\xd8\x88\x8a\x0a\x8a\x85\x60\x2d\x62\xc0\x46\x36\x29\x0c\x2c\x2a\x76\x42\xea\x14\xe9\x2c\x36\xda\xda\x58\x6c\x33\x48\x0a\x8d\xb3\x63\x56\x5c\x4b\xc1\x22\xbb\x56\x3a\x56\xa2\xac\x7f\xc5\x22\x61\x1b\x0d\x49\x8c\x04\x13\x93\x99\x79\x2d\xe6\xce\x3a\x6b\x3e\x38\xe7\x70\xbe\x73\xbe\xff\xf7\x65\x46\xb2\xa6\x03\xe9\x6a\x20\x3d\xeb\xe9\x59\x3f\xa4\x8b\x92\x4d\xd5\xd4\xa6\x9e\x75\x50\xde\x31\xce\xa6\xca\xf5\x19\x65\x67\x26\x00\xa5\x14\xc1\xe8\xe0\x39\xd1\xc9\xb6\x3a\x7d\x5f\xa4\xe7\xb5\xb2\x6a\xe4\x61\x4d\xb6\xd5\x22\xee\x1a\x2b\x38\xaa\x2e\x24\x5d\x4b\xe9\x39\x91\x28\x89\x32\xf1\xbf\x63\x8c\x0b\x16\xf4\xb3\xe1\x64\x39\xe9\xef\xf2\x92\xa1\x5a\x6d\xd9\x82\x50\x56\xdd\x4a\x14\x47\xec\xa8\x9c\x71\x4e\xe5\xd3\x36\xbf\xa4\xad\xbd\xe7\x44\xfa\x92\x8f\xbc\x9c\x3d\x67\xf3\x93\x1b\xd9\x73\x2b\xbf\xf9\x32\x5f\x7b\x25\x1f\xba\x94\x4d\x83\x50\xb2\xa6\x93\x28\xd2\xd5\xb4\x6b\x09\xb2\xe1\x78\xbe\xb3\x9b\x2b\x92\x5f\x24\x3f\x4a\xf6\xdb\xb3\xef\x9b\x19\xe3\x4e\x28\xc5\xff\x24\x7b\xce\x5a\xf6\x9e\x2b\x6e\x63\x5e\x51\xc4\xd0\x9c\xca\xd8\x65\x8d\xe7\xca\x63\xfe\x3c\x68\x7c\x7a\xd6\xc5\xc4\xd1\x9c\xda\x33\xde\xd4\x58\x34\x42\x31\x1b\xe0\xae\x63\x1a\x7f\x78\xd7\xf7\xde\xb7\xa0\x71\xcd\xb0\x3e\x18\xd5\x48\x50\xa9\x2d\xb5\xc6\x87\x65\xac\x76\x53\x5c\xf5\xb6\xa1\xb7\xdc\x56\x2c\xca\xbd\x25\xfc\x6c\xc7\xb2\x17\xfc\x65\xc4\x04\x3c\x22\x8a\x91\xfb\xd4\xae\x39\x65\xd7\xb6\x65\x95\xdf\x8d\x4b\xba\x1a\x4f\x89\x79\x8d\x7d\x77\x3c\xe9\x79\x8b\x06\x6a\xdc\x31\x14\xb5\x62\xe4\x98\xca\x75\x5b\xe5\x69\xa7\x0e\x81\xaf\x1d\xe3\x14\x61\x72\xc1\x25\x4b\x8a\x67\x3d\xee\x88\x47\xdc\x6c\xf3\xf8\xc7\xe7\x06\xe6\x74\xf4\xca\x1b\xfa\xe9\x6a\x9c\x36\x9c\x60\x7b\x4d\x27\x5b\x1e\xc8\x27\x06\xb9\xe8\xdb\x50\xf2\xab\xfb\xb3\xeb\x5c\x06\x6e\xe4\x07\xaf\xb6\xce\x5f\xcf\x96\xa4\x6f\x05\xb2\xa9\x32\x25\x46\x3e\xb6\x92\x8b\xb6\xf9\x8f\x54\x90\xf3\x2e\xe7\x09\xf3\x07\xf7\xbe\x95\x6c\x49\x36\x1c\xcf\xbd\xad\x6e\x3f\x65\x82\xb2\x7c\xe6\xa1\x6c\xd8\xcf\x79\x0f\x72\x88\xa5\x2f\xa6\xef\x51\x66\xd8\x98\x29\x16\x26\x7b\x4a\x91\x7c\x60\x68\x11\xe3\x96\x7d\xa7\x0d\x73\x54\x55\x56\x7d\x35\xb5\xfb\x17\x7e\x62\x09\x19\x85\x1d\x1e\x0c\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x00\x20\x00\x00\x00\x20\x08\x06\x00\x00\x00\x73\x7a\x7a\xf4\x00\x00\x00\xf1\x49\x44\x41\x54\x78\x9c\xed\x97\x41\x16\x83\x20\x0c\x44\x87\xbe\x5e\xc6\x33\xf5\x7c\x5e\xa7\xdb\x1e\x87\x6e\xaa\x8f\x6a\xc8\x8c\x84\xa2\x8b\x66\xe9\x23\x99\x1f\x42\x20\x02\x01\xcb\x33\x72\x9e\x91\x23\x31\x6e\x11\xe7\x1e\xf6\x07\x30\x01\xa2\x75\x0d\x01\x2c\xe2\xbd\x21\x6a\xf1\x76\x00\xe9\x81\xc4\x9c\x5a\xc5\xad\x78\x66\x09\x7a\x42\x94\xfe\x65\xdc\xf5\x5b\xab\x73\x7e\xed\xc1\xd2\xb4\x59\x43\xc4\x29\x80\x15\xc4\x12\xb6\x40\x14\x71\x09\x60\x81\x50\xc5\x01\x00\xcf\x42\xc0\x11\x97\x01\x00\x7b\xcb\x19\x04\x13\x97\x01\x0e\x8b\x97\x02\x93\xaf\x71\xcd\x9b\xb0\xb4\x48\xf6\x8a\xff\x7d\xe4\xb5\x6b\x02\x8c\x10\xf1\x92\xe4\xf7\x40\xb0\x04\x00\xbe\xda\xf2\x14\x00\xaf\x13\xe8\x21\x64\x6d\x14\xf5\xbf\x7e\x1b\x02\x9f\x2c\x9c\x3a\xba\x7e\x3d\x00\xd6\x53\x7c\x00\x62\xfb\x20\x35\x03\xa8\xaf\x5a\x4d\x9c\x41\x5c\x77\x1e\x50\x33\x5f\xd6\xd5\xd6\xb0\x38\x74\x2a\x56\xb7\xbd\x66\x6c\xbc\x73\x67\xc2\xa8\xb8\x0a\x11\xb2\x23\xff\x87\xf2\x0e\xfc\xca\xe4\x33\x30\xd2\x4e\x07\x78\x03\x10\xe5\x84\x0d\xb8\x9e\x6a\x79\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82'
        resp = b"HTTP/1.1 200 OK\r\n" \
               b"Content-Type: text/plain; charset=utf-8\r\n" \
               b"Content-Length: " + str(len(resp_body_favicon)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body_favicon
        return resp

    if url_path == '/':
        # resp_body = f"Emulating Web application. Response for: {url_path!r} page.".encode()
        with open("onePageHtmlWebsite_index.html") as html_page_file:
            text = html_page_file.read()
            text = text.replace('<body>',
                                '<body><a href="/file">Link to the pdf file (open doc).</a><br>'
                                            '<a href="/file_download">Link to the pdf file (download doc).</a>')
            resp_body = text.encode()

        resp = b"HTTP/1.1 200 OK\r\n" \
               b"Content-Type: text/html; charset=utf-8\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp
    elif url_path == '/file':
        with open("file.pdf", mode="rb") as pdf_file:
            resp_body = pdf_file.read()

        resp = b"HTTP/1.1 200 OK\r\n" \
               b"Content-Type: application/pdf\r\n" \
               b"Content-Disposition: inline; filename=file.pdf" + b"\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp
    elif url_path == '/file_download':
        with open("file.pdf", mode="rb") as pdf_file:
            resp_body = pdf_file.read()

        resp = b"HTTP/1.1 200 OK\r\n" \
               b"Content-Type: application/pdf\r\n" \
               b"Content-Disposition: attachment; filename=file.pdf" + b"\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp

    # Other not-defined sub-pages:
    else:
        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] sub-pages are not supported, detected not supported sub-page {url_path}.")
        resp_body = "404 Page not found.".encode()
        resp = b"HTTP/1.1 404 Not Found\r\n" \
               b"Content-Type: text/plain; charset=utf-8\r\n" \
               b"Content-Length: " + str(len(resp_body)).encode() + b"\r\n" \
               b"Connection: close\r\n\r\n" + \
               resp_body
        return resp



def handle_connection(c_socket, c_address) -> None:

    thread_name = threading.current_thread().name
    LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] "
          f"starting to handle the newly setuped connection (remote endpoint: {c_address[0]}:{c_address[1]}).")

    # c_socket:
    #  - the most important object here
    #  - it is the dynamically created client socket
    with c_socket:
        request_data = b""
        chunk = 0
        chunk_size = 1024

        while True:
            chunk += 1
            chunk_start = (chunk - 1) * chunk_size + 1
            chunk_end = chunk * chunk_size
            LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] starting receiving data from the request "
                  f"(chunk {chunk}, bytes: {chunk_start}-{chunk_end}; remote endpoint: {c_address[0]}:{c_address[1]}).")

            # Detecting ending of HTTP headers (request):
            if not b"\r\n\r\n" in request_data:
                data = c_socket.recv(chunk_size)
                request_data += data
                LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] received data from the request (chunk {chunk},"
                             f" bytes: {chunk_start}-{chunk_end}; remote endpoint: {c_address[0]}:{c_address[1]}).")

            if not data or b"\r\n\r\n" in request_data:
                break
        try:
            req_parsed = HttpRequestParser(raw_data=request_data)
            method, path, version = req_parsed.method, req_parsed.path, req_parsed.version
        except Exception:
            LOGGER.exception(f"[Server,{HOST}:{PORT}][{thread_name}] Failed to parse a request "
                             f"(request_data: {request_data}; remote endpoint: {c_address[0]}:{c_address[1]}).")
            client_socket.close()
            return

        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] building environ dictionary with PEP-3333 compliance "
                     f"(remote endpoint: {c_address[0]}:{c_address[1]}).")
        # --- budowa environ (minimalna, ale zgodna z PEP-3333) ---
        environ = {
            'logger': LOGGER,
            'REQUEST_METHOD': method,
            'PATH_INFO': path.split('?', 1)[0],
            'SCRIPT_NAME': '',
            'QUERY_STRING': path.split('?', 1)[1] if '?' in path else '',
            'SERVER_NAME': HOST,
            'SERVER_PORT': str(PORT),
            'wsgi.version': (1, 0),
            'wsgi.input': io.BytesIO(b''),   # tutaj można przekazać body requestu (dla POST itp.)
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': True,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
        }

        # --- definiujemy start_response ---

        def start_response(status, headers, exc_info=None):

            response_headers = "HTTP/1.1 " + str(status) + "\r\n"
            try:
                for name, value in headers:
                    response_headers += f"{name}: {value}\r\n"
            except ValueError:
                breakpoint()

            response_headers += "\r\n"

            LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] sending http headers part of response "
                         f"(remote endpoint: {c_address[0]}:{c_address[1]}).")
            c_socket.sendall(response_headers.encode("utf-8"))


        LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] calling WSGI app object "
                     f"(remote endpoint: {c_address[0]}:{c_address[1]}).")

        # --- wywołanie aplikacji WSGI ---
        result = application(environ, start_response)

        try:

            LOGGER.debug(f"[Server,{HOST}:{PORT}][{thread_name}] sending http body-related part of response "
                         f"(remote endpoint: {c_address[0]}:{c_address[1]}).")
            for data in result:
                # Każdy element z result musi być typu bytes
                if not isinstance(data, (bytes, bytearray)):
                    raise TypeError("WSGI application must yield bytes")
                c_socket.sendall(data)

        finally:
            # Zgodnie z PEP-3333: jeśli obiekt result ma metodę close(), należy ją wywołać
            if hasattr(result, 'close'):
                try:
                    result.close()
                except Exception as e:
                    LOGGER.exception(f"Exception while closing WSGI result ({e})")

        c_socket.close()


# WSGI configuration
########################################################################################################################
import io
import sys
import importlib
ARGV_LEN = len(sys.argv)

if ARGV_LEN in (2, 3):
    app_index = ARGV_LEN - 1
    filename = sys.argv[0]
    application_mod, application_obj_str = sys.argv[app_index].split(":", 1)
    application_module = importlib.import_module(application_mod)
    application = application_module.application
    LOGGER.debug(f"[Server,{HOST}:{PORT}][main] "
                 f"WSGI application was configured (app object: {application_mod}.py:{application_obj_str}).")

else:
    raise RuntimeError("WSGI application has to be declared. Format: APPLICATION_MOD:APPLICATION_OBJ.")
########################################################################################################################

# "Server" socket object - an INET, STREAMing/Listening socket:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    server_socket.bind(SERVER_ADDRESS) # bind the socket to a well-known port
except OSError:
    release_process(PORT)
    import time
    time.sleep(1)
    server_socket.bind(SERVER_ADDRESS)  # bind the socket to a well-known port

server_socket.listen() # become a server socket
LOGGER.debug(f"[Server,{HOST}:{PORT}][main] streaming / listening / INET 'server' socket was configured.")


while True:

    LOGGER.info(f"[Server,{HOST}:{PORT}][main] listening/waiting for connections from outside.")
    client_socket, s_address = server_socket.accept()
    LOGGER.info(f"[Server,{HOST}:{PORT}][main] new connection was accepted by server (details: {HOST}:{PORT} - {s_address[0]}:{s_address[1]}).")

    cst = threading.Thread(target=handle_connection, args=(client_socket, s_address))
    cst.start()


#
# Things done to met WSGI criteria:
# 1. configuration/linking WSGI app to the server
#    like here app object is taken from wsgi_app module
#    python3 http_get_danserv_wsgi.py 9001 wsgi_app:app
#
# 2. handle_connection refactoring
#    first receiving request data from socket (it can be reused later)
#    building environ dictionary with PEP-3333 compliance
#    adding start_response function definition

# 3. calling WSGI app object - splitting sending http headers and body response
#    result = application(environ, start_response)
#    application sends http headers
#
# 4. sending rest of http body data - response
#
