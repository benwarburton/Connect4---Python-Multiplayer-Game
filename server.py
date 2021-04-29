import socket
from _thread import *
import sys
from lib.network import Network

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
PORT = 1224

try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection...")

current_identifier = 1

def unique_client(connection, current_identifier):
    connection.send(bytes(current_identifier))
    message = ''
    while True:
        try:
            data = connection.recv(2048)
            message = data.decode('utf-8')
            if data is None:
                connection.send(str.encode("Ending session"))
            else:
                log = message.split(',')
                id = int(log[0])
                move = str(log[1])
            
            connection.sendall(str.encode(message))
        except:
            break
    
    print("Connection terminated")
    connection.close()
    



# Accepts all new incoming connections
while True:
    '''
    Retrieve details of connected client, while also
    accepting the connection
    '''
    connection, address = s.accept()
    print("Connected!")
    print("Player found: ", current_identifier, address)
    # Start a new thread for each unique client
    start_new_thread(unique_client, (connection, current_identifier))
    current_identifier += 1