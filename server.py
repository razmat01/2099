from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import PodSixNet
import pygame
import openlevel

class catClass():
        speed = 1
        x=0
        y=0

class playerClass():
    

    cat = catClass
    address = ""
    channel = ""
    #cat = cat()
    
        



class ClientChannel(Channel):
    def Network_message(self, data):
        print("Client message:", data['content'])
        message = self.addr, " : ", data['content'] , "\n"
        self.Send({"action":"message","content":message})

    def Network_ping(self,data):
        print("recieved ping from ", myserver.addr)
        self.Send({"action": "return", "content": "ping"})
    
    def Network_updateRequest(self,data):
        i=1
        for player in players:
            self.Send({"action":"catreturn","x":player.cat.x,"y":player.cat.y,"i":i})
            i+=1
        
    def Network_keypress(self,data): #detect keypress for cat
        for player in players:
            if(player.address == self.addr):

                if(data["content"]=="W"):
                    
                    player.cat.y-=player.cat.speed
            
                elif(data["content"]=="S"):
                    player.cat.y+=player.cat.speed

                if(data["content"] == "A"):
                    player.cat.x-=player.cat.speed

                elif(data["content"] == "D"):
                    player.cat.x+=player.cat.speed

    def Network_requestMap(self,data):

        self.Send({"action":"mapReturn","content":"level.dat"})



        
  
class MyServer(Server):
    channelClass = ClientChannel
    def Connected(self, channel, addr):
        print("New connection from address:", addr)
        print("New connection:", channel)
        dummy = playerClass()
        dummy.address = addr
        dummy.channel = channel
        players.append(dummy)
        

players = []
myserver = MyServer(localaddr=("0.0.0.0", 25565))

print("server listening")
level = openlevel.openlevelfile("level.dat")
 #initiate cat object

while True:
    myserver.Pump()
    pygame.time.wait(5)
