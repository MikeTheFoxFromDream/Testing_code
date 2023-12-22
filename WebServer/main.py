import pigpio
import RPi.GPIO as GPIO
import time
import json
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


def passNextBall(delay):
    time.sleep(delay)
    #set DIP pins on S1=ON, S2=OFF, S3=ON
    for x in range(1, 201):
        GPIO.output(EN, GPIO.HIGH)
        GPIO.output(PUL, GPIO.HIGH)
        GPIO.output(PUL, GPIO.LOW)
    return

def aimServo():
    return

def changeMotorSpeed():
    return

def startMode(data):
    global nextDelay
    jsonData = json.loads(data)
    for ball in jsonData["micky"].items():
        temp = str(ball[1]).replace("\'", "\"")
        ballData = json.loads(temp)
        passNextBall(nextDelay)
        nextDelay = int(ballData["delay"])
    return


GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

nextDelay = 0
PUL = 6
DIR = 13
EN = 12
SERVO = 14

GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(SERVO, GPIO.OUT)

servo = GPIO.PWM(SERVO, 50)

server = HTTPServer(("", 8000), RequestHandler)
server.serve_forever()
server.server_close()
