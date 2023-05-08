from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import time
import argparse

# Set up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, default=8000, help="port number (default: 8000)")
parser.add_argument("-r", "--random", type=int, default=1000, help="random delay factor in milliseconds (default: 1000)")
args = parser.parse_args()

# Define the request handler class
class DelayedResponseHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        # Generate a random delay in milliseconds
        delay = random.randint(0, args.random) / 1000
        time.sleep(delay)
        
        # Send the response
        self.send_response(200)
        self.send_header("Delay", delay)
        self.end_headers()

# Set up the server
if __name__ == '__main__':
    with HTTPServer(("", args.port), DelayedResponseHandler) as httpd:
        print("Server started :%s with a max of %dms delay" % (args.port, args.random))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
        print("Server stopped")

