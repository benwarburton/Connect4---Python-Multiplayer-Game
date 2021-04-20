import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname()
PORT = 1223

try:
    s.connect((server, PORT))
except socket.error as e:
    print(str(e))

test_msg = s.recv(1024).decode("utf-8")

print(test_msg)