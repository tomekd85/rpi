import socket

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


HOST = '127.0.0.1'        # Symbolic name meaning all available interfaces
PORT = 58888              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    socket_loop = True
    special_char = []
    while socket_loop:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                for int_el in data:
                    el = bytes([int_el])
                    if el == b"\x1b" or special_char:
                        special_char.append(int_el)
                        key = bytes(special_char)
                        if key in special_keys:
                            special_char = []
                        elif len(special_char) >= 3:
                            special_char = []
                        else:
                            continue
                    else:
                        key = data

                if el == b"q":
                    socket_loop = False
                    conn.close()
                    break
                func = actions.get(key, received)
                func(key)


