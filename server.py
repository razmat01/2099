from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import PodSixNet
import pygame


class ClientChannel(Channel):
    def Network_message(self, data):
        #print("Received data from client:", data)
        # Print the message received from the client
        
        print("Client message:", data['content'])
    

class MyServer(Server):
    channelClass = ClientChannel

    

    def Connected(self, channel, addr):
        print("New connection from address:", addr)
        print("New connection:", channel)

myserver = MyServer(localaddr=("0.0.0.0", 25565))

print("server listening")
while True:



    myserver.Pump()
    pygame.time.wait(50)
