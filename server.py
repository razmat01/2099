from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import os

class ClientChannel(Channel):
    def Network(self, data):
        # Handle incoming data from a client here
        def Network(self, data):
            if data["action"] == "move":
                print("hello")
        # Handle the move action here

        pass

class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print("New connection:", channel)

myserver = MyServer()
while True:
    myserver.Pump()
    sleep(0.01)
