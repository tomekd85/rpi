from collections import deque
import time
import actions

class Mover():
    def __init__(self, refresh_rate):
        self.move_duration = refresh_rate
        self.keep_going = True
        self.moves = deque()
        self.queue_size = 5

    def move(self):
        while self.keep_going:
            num_of_moves_in_queue = len(self.moves)

            if self.queue_size > num_of_moves_in_queue > 1:
                move1 = self.moves.pop()
                move2 = self.moves.pop()
                move = move1 if move1 == move2 else "Stop"
            elif num_of_moves_in_queue >= self.queue_size:
                move = self.moves.pop()
                self.moves.clear()
            else:
                move = "Stop"

            func = actions.actions.get(move, actions.received)
            func(move)
            time.sleep(self.move_duration)

        actions.robot.finish_work()

    def stop_moving(self):
        self.keep_going = False


