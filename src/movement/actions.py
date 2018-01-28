# from gpio_emulation.moverobot import Baymax

from movement.mover import Mover

def received(el):
    print("Received {}".format(el))


special_keys = (b"\x1b[A", b"\x1b[B", b"\x1b[C", b"\x1b[D")

robot =Mover()

actions = {b"w": robot.move_forward,
           b"a": robot.turn_left,
           b"s": robot.move_backward,
           b"d": robot.turn_right,
           "Stop" : robot.stop,
           b"\x1b[A": robot.move_forward,
           b"\x1b[B": robot.move_backward,
           b"\x1b[C": robot.turn_right,
           b"\x1b[D": robot.turn_left
          }

