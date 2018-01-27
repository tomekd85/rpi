from collections import deque
import time
from movement import actions, consts


class Mover:
    # Singletone design pattern from:
    # http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    __instance = None

    def __new__(cls, refresh_rate=None):
        if Mover.__instance is None:
            Mover.__instance = object.__new__(cls)
        Mover.__instance.move_duration = refresh_rate
        return Mover.__instance

    def __init__(self, refresh_rate=None):
        self.move_duration = refresh_rate
        self.keep_going = True
        self.moves = deque()
        self.queue_size = 5

    def set_move_duration(self, value):
        self._move_duration = value or consts.Movement.REFRESH_RATE

    def get_move_duration(self):
        return self._move_duration

    move_duration = property(get_move_duration, set_move_duration)

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


