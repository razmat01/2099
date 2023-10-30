from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import PodSixNet
import pygame

class cat():
    speed = 1
    x=0
    y=0


class ClientChannel(Channel):
    #instances = []


    
    def Network_message(self, data):
        print("Client message:", data['content'])
        message = self.addr, " : ", data['content'] , "\n"
        self.Send({"action":"message","content":message})

    def Network_ping(self,data):
        print("recieved ping from ", myserver.addr)
        self.Send({"action": "return", "content": "ping"})
    
    def Network_updateRequest(self,data):
        print("update requested")
        self.Send({"action":"catreturn","x":cat.x,"y":cat.y})
        
    def Network_keypress(self,data):
        print("key presed")

        if(data["content"]=="W"):
            cat.y-=cat.speed
        elif(data["content"]=="S"):
            cat.y+=cat.speed
        if(data["content"] == "A"):
            cat.x-=cat.speed
        elif(data["content"] == "D"):
            cat.x+=cat.speed
    

class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print("New connection from address:", addr)
        print("New connection:", channel)

myserver = MyServer(localaddr=("0.0.0.0", 25565))

print("server listening")

cat1 =cat()

while True:
    myserver.Pump()
    pygame.time.wait(50)
