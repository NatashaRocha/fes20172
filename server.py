#!/usr/bin/env python
 
import json
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
 
HOST = "0.0.0.0"
PORT = 8000
FILENAME = "provas.json"
 
def parse_json(self):
    print(self.decode("utf8"))


    with open(FILENAME, "r") as inputFile:
        array = json.load(inputFile)
        array.append(json.loads(self.decode("utf8")))

    with open(FILENAME, "w") as outputFile:
        json.dump(array, outputFile, indent=4)
 
class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        parse_json(post_body)

        return
 
if __name__ == "__main__":
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, RequestHandler)
 
    print(time.asctime(), "Server Starts - %s:%s" % server_address)
 
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
 
    httpd.server_close()
 
    print(time.asctime(), "Server Stops - %s:%s" % server_address)
 