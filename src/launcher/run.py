import asyncio
import threading
from asyncioServer.asyncioServer import EchoServerClientProtocol

from movement import actions, rpiMover

if __name__ == "__main__":
    # Run moving functionallity
    mover = rpiMover.Mover()
    thread = threading.Thread(target=mover.move, name="rpiMover")
    thread.start()

    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
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