from PodSixNet.Connection import ConnectionListener

class MyClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))

    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def SendData(self, data):
        self.Send(data)

myclient = MyClient("60.242.224.77", 1337)
while True:
    myclient.SendData({"message":"hello"})

    myclient.Pump()