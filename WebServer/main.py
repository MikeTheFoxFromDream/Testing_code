import time
from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    # Prozatím jen pro testování funkčnosti avšak v budoucnu se bude možná zde aplikace rozvíjet
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

    # Zde čekáme na POST request s JSON souborem obsahujícím informace o
    # herním módu (nadhozy, velikost stolu, opakování, etc)
    def do_POST(self):
        self.send_response(200)
        messageLength = self.headers.get("Content-length")
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("\nData received \n\n".encode())
        time.sleep(0.01)
        startMode(self.rfile.read(int(messageLength)))
        return


def startMode(data):
    print(data)
    return

# Zde nastavujem PORT na kterém server poběží a zároveň jej zpustíme
PORT = 8000
server = HTTPServer(("", 8000), RequestHandler)
server.serve_forever()
server.server_close()
