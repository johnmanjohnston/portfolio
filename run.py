from http.server import HTTPServer, BaseHTTPRequestHandler
import os

# Get port number from the PORT environment varaible or 3000 if not specified
port = os.getenv('PORT', 3000)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.wfile)
        self.wfile.write(bytes("<body><p>This is a test.</p>",  encoding="utf-8"))
        self.wfile.close()

server = HTTPServer(('0.0.0.0', port), MyServer)
server.serve_forever()