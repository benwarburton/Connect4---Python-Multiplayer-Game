import socket
import pygame

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname()
PORT = 1234

try:
    s.connect((server, PORT))
except socket.error as e:
    print(str(e))

