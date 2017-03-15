import socketserver
import actions

class MyTCPServer(socketserver.TCPServer):
    def serve_forever(self):
        self.serve_forever_loop = True
        while self.serve_forever_loop:
            self.handle_request()


class RequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.special_char = []

    def handle(self):
        self.handle_loop = True
        while self.handle_loop:
            data = self.request.recv(1024)
            print(data)
            for int_el in data:
                el = bytes([int_el])
                if el == b"\x1b" or self.special_char:
                    self.special_char.append(int_el)
                    key = bytes(self.special_char)
                    if key in actions.special_keys:
                        self.special_char = []
                    elif len(self.special_char) >= 3:
                        self.special_char = []
                    else:
                        continue
                else:
                    key = data
            if el == b"q":
                self.handle_loop = False
                self.server.serve_forever_loop = False
                break
            func = actions.actions.get(key, actions.received)
            func(key)

with MyTCPServer(("127.0.0.1", 58888), RequestHandler) as server:
    server.serve_forever()

