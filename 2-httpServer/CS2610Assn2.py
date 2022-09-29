from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import time


class CS2610Assn2(BaseHTTPRequestHandler):
    def dataHelper(self, type_location, fileName, requestHandler, code):
        header = f"Server: Carter's Server\nDate: {time.strftime('%c')}\nConnection: close\nCache-Control: max-age=10\n"
        if code != "301 Moved Permanently":
            if os.path.isfile(fileName):
                f = open(fileName, "rb")
                data = f.read()
                f.close()
                header += f"Content-type: {type_location}\n"
                header += f"Content-length: {len(data)}\n"
            else:
                return
        else:
            header += f"Location: {type_location}\n"
        header += "\n"
        requestHandler.wfile.write(bytes(f"HTTP/1.1 {code}\n" + header, encoding="utf-8"))
        if code != "301 Moved Permanently":
            requestHandler.wfile.write(data)

    def do_GET(self):
        # pages
        if self.path == "/index.html": # index
            self.dataHelper("text/html", "index.html", self, "200 OK")
        elif self.path == "/about.html":
            self.dataHelper("text/html", "about.html", self, "200 OK")
        elif self.path == "/techtips+css.html":
            self.dataHelper("text/html", "techtips+css.html", self, "200 OK")
        elif self.path == "/techtips-css.html":
            self.dataHelper("text/html", "techtips-css.html", self, "200 OK")
        elif self.path == "/style.css":
            self.dataHelper("text/css", "style.css", self, "200 OK")
        elif self.path == "/teapot": # ERROR 418
            self.dataHelper("text/html", "error418.html", self, "418 I'm a teapot")
        elif self.path == "/forbidden": # ERROR 403
            self.dataHelper("text/html", "error403.html", self, "403 Forbidden")
        elif self.path == "/debugging":
            # create page
            page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>Debug</title></head><body>
                <h1>Debugging</h1><p style="white-space: pre-line;">"""
            page += "Server Version: " + self.server_version + "\n"
            page += "Date & Time: " + time.strftime('%c') + "\n"
            page += "Client IP & port: " + str(self.client_address[0]) + ":" + str(self.client_address[1]) + "\n"
            page += "Requested Path: " + self.path + "\n"
            page += "HTTP Requested Type: " + self.requestline + "\n"
            page += "HTTP Version of Requested: " + self.request_version + "\n"
            page += "Ordered list of HTTP request headers: "
            for i in self.headers:
                page += str(i) + "; "
            page += """</p>\n</body>\n</html>"""
            data = bytes(page, encoding="utf-8")
            # create header
            header = f"Server: Carter's Server\nDate: {time.strftime('%c')}\nConnection: close\nCache-Control: max-age=10\n"
            header += f"Content-type: text/html\n"
            header += f"Content-length: {len(data)}\n"
            header += "\n"
            # write
            self.wfile.write(bytes("HTTP/1.1 200 OK\n" + header, encoding="utf-8"))
            self.wfile.write(data)
        # 301 Redirects
        elif self.path in ["/", "/index", "/about", "/tips", "/help"] or self.path[0:4] == "/bio":
            if self.path in ["/", "/index"]:
                location = "index.html"
            elif self.path == "/about" or self.path[0:4] == "/bio":
                location = "about.html"
            elif self.path == "/tips":
                location = "techtips+css.html"
            elif self.path == "/help":
                location = "techtips-css.html"
            self.dataHelper(location,  "", self, "301 Moved Permanently")
        # images/icons
        elif self.path == "/favicon.ico":
            self.dataHelper("image/x-icon", "favicon.ico", self, "200 OK")
        elif self.path in ["/imgs/rubiks_before_weight_loss.jpg", "/rubiks_before_weight_loss.jpg", "/rubiks_bwl"]:
            self.dataHelper("image/jpeg", "imgs/rubiks_before_weight_loss.jpg", self, "200 OK")
        elif self.path in ["/imgs/rubiks_cube.jpg", "/rubiks_cube.jpg", "/rubiks_cube"]:
            self.dataHelper("image/jpeg", "imgs/rubiks_cube.jpg", self, "200 OK")
        elif self.path in ["/imgs/rubiks_w_friend.jpg", "/rubiks_w_friend.jpg", "/rubiks_wf"]:
            self.dataHelper("image/jpeg", "imgs/rubiks_w_friend.jpg", self, "200 OK")
        else: # ERROR 404 
            self.dataHelper("text/html", "error404.html", self, "404 Page Not Found")


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    print(f"Serving from http://{server_address[0]}:{server_address[1]}")
    print("Press Ctrl-C to quit\n")
    try:
        HTTPServer(server_address, CS2610Assn2).serve_forever()
    except KeyboardInterrupt:
        print(" Exiting")
        exit(0)