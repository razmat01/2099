from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import os

class ClientChannel(Channel):
    def Network(self, data):
        print("Received data from client:", data)
        # Handle the data further if necessary


class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print("New connection:", channel)

myserver = MyServer()
while True:
    myserver.Pump()
    sleep(0.01)
