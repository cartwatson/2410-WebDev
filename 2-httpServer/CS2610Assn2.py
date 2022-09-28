from http.server import HTTPServer, BaseHTTPRequestHandler
from importlib.resources import path
import time
from urllib.request import DataHandler


class CS2610Assn2(BaseHTTPRequestHandler):
    def dataHelper(self, header, type, fileName, requestHandler):
        f = open(fileName, "rb")
        data = f.read()
        f.close()
        header += f"Content-type: {type}\n"
        header += f"Content-length: {len(data)}\n"
        header += "\n"
        requestHandler.wfile.write(bytes("HTTP/1.1 200 OK\n" + header, encoding="utf-8"))
        requestHandler.wfile.write(data)

    # TODO: Handle HTTP GET requests
        # TODO: Response headers
    def do_GET(self):
        header = f"Server: Carter's Server\nDate: {time.strftime('%c')}\nConnection: close\nCache-Control: max-age=10\n"
        # PAGES --------------------------------------------------------------------------------------------------------------
        if self.path in ["/", "/index", "/index.html"]: # index
            self.dataHelper(header, "text/html", "index.html", self)
        elif self.path in ["/about.html", "/about"] or self.path[0:4] == "/bio":
            self.dataHelper(header, "text/html", "about.html", self)
        elif self.path in ["/tips", "/techtips+css.html"]:
            self.dataHelper(header, "text/html", "techtips+css.html", self)
        elif self.path in ["/help", "/techtips-css.html"]:
            self.dataHelper(header, "text/html", "techtips-css.html", self)
        # IMAGES -------------------------------------------------------------------------------------------------------------
        # elif self.path == "/favicon.ico":
        #     f = open("favicon.ico", "rb")
        #     data = f.read()
        #     f.close()
        #     header += "Content-type: image/ico\n"
        #     header += f"Content-length: {len(data)}\n"
        #     header += "\n"
        #     self.wfile.write(bytes("HTTP/1.1 200 OK\n" + header, encoding="utf-8"))
        #     self.wfile.write(data)
        elif self.path in ["/imgs/rubiks_before_weight_loss.jpg", "/rubiks_before_weight_loss.jpg", "/rubiks_bwl"]:
            self.dataHelper(header, "image/jpeg", "imgs/rubiks_before_weight_loss.jpg", self)
        elif self.path in ["/imgs/rubiks_cube.jpg", "/rubiks_cube.jpg", "/rubiks_cube"]:
            self.dataHelper(header, "image/jpeg", "imgs/rubiks_cube.jpg", self)
        elif self.path in ["/imgs/rubiks_w_friend.jpg", "/rubiks_w_friend.jpg", "/rubiks_wf"]:
            self.dataHelper(header, "image/jpeg", "imgs/rubiks_w_friend.jpg", self)
        else: # ERROR 404 
            self.dataHelper(header, "text/html", "error404.html", self)

    # TODO: debugging
        # following info
        # instance variables
        # TODO: server version string
        # TODO: servers current date and time
        # TODO: client IP & port number 
        # TODO: path requested
        # TODO: HTTP request type
        # TODO: HTTP version of request
        # TODO: ordered list of HTTP request headers
    # TODO: 418 Teapot
        # TODO: usual set of HTTP headers
        # TODO: HTML document both short and stout
        # TODO: link back to main
    # TODO: 403 forbidden
        # TODO: tell user they are forbidden
        # TODO: link back to main -------- not required

    pass


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn2).serve_forever()
    except KeyboardInterrupt:
        print(" Exiting")
        exit(0)