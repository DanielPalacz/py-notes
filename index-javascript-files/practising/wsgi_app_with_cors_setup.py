def app(environ, start_response):
    # Obsługa preflight (OPTIONS)
    if environ['REQUEST_METHOD'] == 'OPTIONS':
        headers = [
            ("Access-Control-Allow-Origin", "*"),
            ("Access-Control-Allow-Methods", "GET, POST, OPTIONS"),
            ("Access-Control-Allow-Headers", "Content-Type, X-Custom-Header"),
        ]
        start_response("200 OK", headers)
        return [b""]

    data = b"Hello, World!\n"
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data))),
            ("Access-Control-Allow-Origin", "*")
    ])
    return iter([data])
