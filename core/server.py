from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = ""
PORT = 8080

class MainHTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


        self.wfile.write(bytes("<h1>asdasd</h1>"))



server = HTTPServer(())