import sys, os
parent = os.path.pardir
sys.path.append(parent)

from gpio_emulation.moverobot import Baymax


def go_forward(key):
    print("going forward")


def go_backward(key):
    print("going back")


def go_left(key):
    print("turning left")


def go_right(key):
    print("turning right")


def stop_moving(key):
    print("Stopped moving")


def received(el):
    print("Received {}".format(el))

special_keys = (b"\x1b[A", b"\x1b[B", b"\x1b[C", b"\x1b[D")

robot = Baymax()

actions = {b"w": robot.move_forward,
           b"a": robot.turn_left,
           b"s": robot.move_backward,
           b"d": robot.turn_right,
           "Stop" : robot.stop,
           b"\x1b[A": go_forward,
           b"\x1b[B": go_backward,
           b"\x1b[C": go_right,
           b"\x1b[D": go_left
          }

