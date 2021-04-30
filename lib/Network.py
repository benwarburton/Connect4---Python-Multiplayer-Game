import socket

class Network:

    client_id = ''

    def __init__(self, host:str):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = 1224
        self.address = (self.host, self.port)
        self.identifier = self.connect()
        

    def connect(self) -> str:
        self.client.connect(self.address)
        msg = self.client.recv(2048).decode()
        self.client_id = msg
        return msg

    def send_data(self, data:str) -> str:
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(2048).decode()
            return response
        except socket.error as e:
            print(str(e))
            return str(e)

