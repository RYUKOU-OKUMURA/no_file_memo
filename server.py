#!/usr/bin/env python3
"""
Simple HTTP server for No File Memory application
"""
import http.server
import socketserver
import sys
import os

PORT = 8080

class MemoTuckHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        sys.stdout.write(f"{self.log_date_time_string()} - {format%args}\n")
        sys.stdout.flush()

    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

if __name__ == "__main__":
    # Change to the webapp directory
    os.chdir('/home/user/webapp')
    
    # Create and start server
    with socketserver.TCPServer(("0.0.0.0", PORT), MemoTuckHandler) as httpd:
        print(f"No File Memory server running on port {PORT}")
        print(f"Access the application at http://localhost:{PORT}/memotuck.html")
        sys.stdout.flush()
        httpd.serve_forever()