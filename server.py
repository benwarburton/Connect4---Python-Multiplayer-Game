import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ''
PORT = 1223

self_ip = socket.gethostbyname(server)

try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection...")

current_id = '0'

