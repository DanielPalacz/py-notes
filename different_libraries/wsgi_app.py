import time
import threading

class HeaderInjectionMiddleware:
    def __init__(self, app, header_name="X-Powered-By", header_value="DanWSGI"):
        self.app = app
        self.header_name = header_name
        self.header_value = header_value

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers.append((self.header_name, self.header_value))
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)


class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        start = time.perf_counter()
        result = self.app(environ, start_response)

        def result_wrapper():
            try:
                for chunk in result:
                    yield chunk
            finally:
                elapsed = (time.perf_counter() - start) * 1000
                thread_name = threading.current_thread().name
                environ.get("logger").debug(
                    f"[Server,{environ['SERVER_NAME']}:{environ['SERVER_PORT']}][{thread_name}/TimingMiddleware] "
                    f"sending body response for '{environ.get('PATH_INFO', '')}' endpoint took {elapsed:.2f} ms")

                if hasattr(result, "close"):
                    result.close()

        return result_wrapper()


@TimingMiddleware
@HeaderInjectionMiddleware
def application(environ, start_response):
    thread_name = threading.current_thread().name
    environ.get("logger").debug(f"[Server,{environ['SERVER_NAME']}:{environ['SERVER_PORT']}][{thread_name}/application] "
                                    f"running WSGI app code.")

    path = environ.get('PATH_INFO', '/')
    if path == '/':
        status = '200 OK'
        response_body = b"<html><head></head<body>Hello from custom WSGI server!</body></html>"
    else:
        status = '404 Not Found'
        response_body = b"<html><head></head<body>Page not found.</body></html>"

    response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(response_body))),
                        ('Connection', 'close')]
    start_response(status, response_headers)
    return [response_body]