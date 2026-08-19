import http.server
import socketserver
import os
from urllib.parse import urlparse

PORT = 5000

ROUTE_MAP = {
    "/": "index.html",
    "/ChrisCompton": "teams.html",      # ← Your main phishing page
}

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse and remove query string
        parsed_path = urlparse(self.path)
        clean_path = parsed_path.path.rstrip("/")

        if clean_path in ROUTE_MAP:
            self.path = "/" + ROUTE_MAP[clean_path]
        
        return super().do_GET()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Serve files from current folder
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"✅ Server running on http://localhost:{PORT}")
        print("Access example: http://localhost:3009/sustainable-docs?email=test@company.com")
        httpd.serve_forever()