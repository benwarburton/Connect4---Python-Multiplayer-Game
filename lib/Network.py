import socket

class Network:
    def __init__(self, host:str) -> Network():
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.port = 1234
        self.address = (host, port)
        self.id = self.connect()

    def connect(self) -> str:
        self.client.connect(self.address)
        return self.client.recv(2048).decode()

    def move(self, data:str) -> str:
        try:
            self.client.send(str.encode(data))
            response = self.client.recv(512).decode()
            return response
        except socket.error as e:
            print str(e)
            return str(e)

