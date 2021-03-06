import unittest
import asyncio

class TestEventLoop(unittest.TestCase):

    def test_event_loop_start(self):
        def _close_loop(loop):
            loop.stop()
        try:
            loop = asyncio.get_event_loop()
            loop.call_soon(_close_loop, loop)
            loop.run_forever()
        finally:
            self.assertTrue(True)

    def test_event_loop_not_running_status(self):
        loop = asyncio.get_event_loop()
        self.assertFalse(loop.is_closed())

    def test_event_loop_running_status(self):
        def _check_running(loop):
            self.assertTrue(loop.is_running())
            loop.stop()
        loop = asyncio.get_event_loop()
        loop.call_soon(_check_running, loop)
        loop.run_forever()

    @unittest.skip
    def test_TCP_Server(self):
        exit_sign = 'q'
        read_sign = ''
        while read_sign != exit_sign:
            if read_sign == "":
                read = rsock.recv(100)
            read_sign = "q"



if __name__ == '__main__':
    unittest.main()
