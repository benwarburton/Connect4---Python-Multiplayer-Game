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

def unique_client(connection):
    return







# Accepts all new incoming connections
while True:
    '''
    Retrieve details of connected client, while also
    accepting the connection
    '''
    connection, address = s.accept()
    print("New connection: ", address)

    # Start a new thread for each unique client
    start_new_thread(unique_client, (connection,))