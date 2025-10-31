# cors_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Dodaj nagłówki CORS
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

# Uruchom serwer na porcie 8000
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    # httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Serving with CORS at http://127.0.0.1:8000")
    httpd.serve_forever()
