from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import PodSixNet
import pygame


class ClientChannel(Channel):
    instances = []
    def Network_message(self, data):
        print("Client message:", data['content'])
        message = self.addr, " : ", data['content'] , "\n"
        self.Send({"action":"message","content":message})

    def Network_ping(self,data):
        print("recieved ping from ", myserver.addr)
        self.Send({"action": "return", "content": "ping"})
    

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
