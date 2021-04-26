import socket
from _thread import *
import sys
import Network

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = socket.gethostname()
PORT = 1234

try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

s.listen(1)
print("Waiting for a connection...")

user_count = 0

def unique_client(connection):
    connection.send(bytes("Test message", "utf-8"))
    user_count += 1



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