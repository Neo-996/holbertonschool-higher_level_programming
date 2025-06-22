#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set common headers helper
        def send_json_response(data, status=200):
            self.send_response(status)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        if self.path == '/':
            # Simple text response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Serve JSON data
            data = {"name": "John", "age": 30, "city": "New York"}
            send_json_response(data)
        elif self.path == '/status':
            # Return API status text
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            # Return info JSON
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            send_json_response(info)
        else:
            # 404 Not Found for any other endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', 8000)  # Listen on all interfaces, port 8000
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
