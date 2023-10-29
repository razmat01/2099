from PodSixNet.Connection import ConnectionListener

class MyClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def SendData(self, data):
        self.Send(data)

myclient = MyClient("localhost", 1337)
while True:
    myclient.SendData({"message":"hello"})

    myclient.Pump()