import unittest
import asyncio

class TestEventLoop(unittest.TestCase):

    def test_event_loop_start(self):
        loop = asyncio.AbstractEventLoop()
        loop.run_forever()
        loop.close()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
