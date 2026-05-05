import socket
import threading
from sys import argv
import psutil
import logging


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


        #
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

    LOGGER.debug(f"[Server,{HOST}:{PORT}][main] listening/waiting for connections from outside.")
    client_socket, s_address = server_socket.accept()
    LOGGER.info(f"[Server,{HOST}:{PORT}][main] new connection was accepted by server (details: {HOST}:{PORT} - {s_address[0]}:{s_address[1]}).")

    cst = threading.Thread(target=handle_connection, args=(client_socket, s_address))
    cst.start()


#
# Things done to met WSGI criteria:
# 1. configuration/linking WSGI app to the server
#    like here app object is taken from wsgi_app module
#    python3 http_get_danserv_wsgi.py 9001 wsgi_app:application
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
