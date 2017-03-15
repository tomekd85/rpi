def go_forward(key):
    print("going forward")

def go_backward(key):
    print("going back")

def go_left(key):
    print("turning left")

def go_right(key):
    print("turning right")

def received(el):
    print("Received {}".format(el))

special_keys = (b"\x1b[A", b"\x1b[B", b"\x1b[C", b"\x1b[D")


actions = {b"w": go_forward,
           b"a": go_left,
           b"s": go_backward,
           b"d": go_right,
           b"\x1b[A": go_forward,
           b"\x1b[B": go_backward,
           b"\x1b[C": go_right,
           b"\x1b[D": go_left
          }


