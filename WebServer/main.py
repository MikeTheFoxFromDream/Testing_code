from http.server import HTTPServer, BaseHTTPRequestHandler


class requestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

        output = ""
        output += "<html><body>"
        output += "<h1>Is JSON readable or breedable</h1>"
        output += "</body></html>"
        self.wfile.write(output.encode())
        return

    def do_POST(self):
        self.send_response(200)
        print(self.rfile.read())
        return


PORT = 9000
server = HTTPServer(("", 9000), requestHandler)
server.serve_forever()
server.server_close()
