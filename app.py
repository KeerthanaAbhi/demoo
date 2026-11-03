from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class ApplicationHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"SERVICERUNNING\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print(format_string % args)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print("SERVICERUNNING", flush=True)
    print(f"Application listening on port {port}", flush=True)
    HTTPServer(("0.0.0.0", port), ApplicationHandler).serve_forever()
