import socket

class Network:

    client_id = ''

    #Initialize the client, host address, port, and identifier information 
    def __init__(self, host:str):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = 1224
        self.address = (self.host, self.port)
        self.identifier = self.connect()
        
    #SEt up the client to connect to the given host address, as well as get the client id and return it 
    def connect(self) -> str:
        self.client.connect(self.address)
        msg = self.client.recv(3).decode()
        self.client_id = msg
        return msg

    #Send the date of the client to the server when asked, if unable to, print the socket error from the try/catch
    def send_data(self, data:str) -> str:
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(3).decode()
            return response
        except socket.error as e:
            print(str(e))
            return str(e)
    
    #Server/Client awaits for the date to be decoded and returned, if unable to do so, print the socket error from the try/catch
    def await_data(self):
        while True:
            data = self.client.recv(3)
            message = data.decode('utf-8')
            if message is not None:
                return message
            



