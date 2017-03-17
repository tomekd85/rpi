import socketserver
import rpiMover
import actions
import threading

class MyTCPServer(socketserver.TCPServer):
    def serve_forever(self):
        self.serve_forever_loop = True
        while self.serve_forever_loop:
            self.handle_request()


class RequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        self.special_char = []
        self.mover = rpiMover.Mover(0.1)
        thread = threading.Thread(target = self.mover.move)
        thread.start()


    def handle(self):
        self.handle_loop = True
        #self.last_key = ""
        while self.handle_loop:
            data = self.request.recv(1024)
            print(data)
            key = self._collect_key(data)
            if key == b"q":
                self.handle_loop = False
                self.server.serve_forever_loop = False
                self.mover.keep_going = False
                break
            #elif key != self.last_key:
            #    actions.stop_moving()
            self.mover.moves.appendleft(key)
            #func(key)

    def _collect_key(self, data):
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
        return key


with MyTCPServer(("127.0.0.1", 58888), RequestHandler) as server:
    server.serve_forever()

