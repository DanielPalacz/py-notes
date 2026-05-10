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
