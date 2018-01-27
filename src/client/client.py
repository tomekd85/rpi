import sys, os
# Extend client path
extended_path = os.path.abspath(__file__)
parent = os.path.sep.join(extended_path.split(os.path.sep)[:-2])
sys.path.append(parent)

import socket
from utils.getch import getch

HOST = 'localhost' #'192.168.0.6'       # The remote host
PORT = 58888             # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    client_loop = True
    while client_loop:
        data = getch()
        s.sendall(bytes(data, encoding="utf8"), socket.MSG_WAITALL)
        if data == "q":
            break

print("Client closed")

