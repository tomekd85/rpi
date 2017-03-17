from collections import deque
import time
import actions

class Mover():
    def __init__(self, refresh_rate):
        self.move_duration = refresh_rate
        self.keep_going = True
        self.moves = deque()
        self.queue_size = 10

    def move(self):
        while self.keep_going:
            print("Moves = {}".format(self.moves))
            if self.queue_size > len(self.moves) > 0:
                move = self.moves.pop()
            elif len(self.moves) > self.queue_size:
                for count in range(5):
                    self.moves.pop()
            else:
                move = "Stop"

            func = actions.actions.get(move, actions.received)
            func()
            time.sleep(self.move_duration)

        actions.robot.finish_work()
