from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class DarajaCallbackHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        try:
            data = json.loads(body)
            print(f":inbox_tray: Callback at {self.path}")
            print(json.dumps(data, indent=2))
        except:
            print(":warning: Invalid JSON")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'OK')
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, DarajaCallbackHandler)
    print(":white_check_mark: Server running on http://localhost:8000")
    httpd.serve_forever()
if __name__ == '__main__':
    run()






