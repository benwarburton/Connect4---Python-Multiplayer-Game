import socket
from _thread import *
import sys
from lib.network import Network

#Creates the sockets to be used
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Sets up the server and its port that clients will connect to
server = 'localhost'
PORT = 1224

#Binds the server and port, if there is ever an error, it will print out the error message from the try/catch 
try:
    s.bind((server, PORT))
except socket.error as e:
    print(str(e))

#Server will listen and wait for the connections of the clients
s.listen(2)
print("Waiting for a connection...")

current_identifier = '1'

#This creates the unique clients and gives them encoded identifiers. This also ensures that we have unique clients altogether that are not from the same computer. 
def unique_client(connection, current_identifier):
    connection.send(str.encode(current_identifier))
    message = ''
    #Gets the data connection and decode its message, if there is no data, the session is ended immediately. Otherwise, it will encode the message. If there is an error with the socket
    #print the message from the try/catch exception
    while True:
        try:
            data = connection.recv(2048)
            message = data.decode('utf-8')
            if data is None:
                connection.send(str.encode("Ending session"))
            else:
                connection.sendall(str.encode(message))
        except socket.error as e:
            print(str(e))
            break
    
    #Prints to the console notifying the connection is terminated and promptly closes the connection
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
    current_identifier = str(int(current_identifier) + 1)