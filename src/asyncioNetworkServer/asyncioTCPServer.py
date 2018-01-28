import asyncio
import threading

from movement import actions, rpiMover, consts


class EchoServerClientProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.special_char = []
        self.mover = rpiMover.Mover(consts.Movement.REFRESH_RATE)

        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        key = self._collect_key(data)
        if key == b"q":
            self.mover.stop_moving()

        self.mover.moves.appendleft(key)

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
                    key = b"" 
            else:
                key = data
        return key


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    # Each NetworkClient connection will create a new protocol instance
    coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 58888)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
