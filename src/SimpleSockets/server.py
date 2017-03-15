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

special_keys = (b"\x1b", b"\x1b", b"\x1b", b"\x1b")


actions = { b"w": go_forward,
            b"a": go_left,
            b"s": go_backward,
            b"d": go_right
            }

actions.setdefault(received)

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
                el = data
                #for el in data:
                #    el = bytes(el)
                   # if b"\x1b" == el or special_char:
                   #     special_char.append(el)
                   #     key = b"".join(special_char)
                   #     if key in special_keys or len(key) >= 3:
                   #         special_char = []

                if b"q" == el:
                    socket_loop = False
                    conn.close()
                    break
                else:
                    key = el
                print(key)
                func = actions.get(key, received)
                print(func)
                func(key)


