from time import sleep
from PodSixNet.Server import Server
from PodSixNet.Channel import Channel
import PodSixNet
import pygame
import openlevel

allUnits = []

class unitClass():
    def __init__(self):
        allUnits.append(self)

    class soldierClass():
        id=len(allUnits)
        type="soldier"
        movement = 3
        x=0
        y=0
        
        attachedPlayer = 0

        def __init__(self):
            allUnits.append(self)



class catClass():
        speed = 1
        x=0
        y=0

class playerClass():
    soldier = unitClass.soldierClass
    soldier.x = 600
    soldier.y = 400
    address = ""
    channel = ""

    

class ClientChannel(Channel):
    def Network_message(self, data):
        print("Client message:", data['content'])
        message = self.addr, " : ", data['content'] , "\n"
        self.Send({"action":"message","content":message})

    def Network_ping(self,data):
        print("recieved ping from ", myserver.addr)
        self.Send({"action": "return", "content": "ping"})
    
    def Network_updateRequest(self,data):
        i=0
        #print("update requested")
        print(allUnits)
        for i in range(len(allUnits)):
            print("update for unit ",allUnits[i].id)
            print("cords ",allUnits[i].x, " ",allUnits[i].y)
            self.Send({"action":"updateReturn","type":allUnits[i].type,"player":allUnits[i].attachedPlayer,"x":allUnits[i].x,"y":allUnits[i].y,"id":allUnits[i].id})
        
    def Network_keypress(self,data): #detect keypress for cat
        print("sd")

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
        newUnit = unitClass.soldierClass()
        

players = []
myserver = MyServer(localaddr=("0.0.0.0", 25565))

print("server listening")
level = openlevel.openlevelfile("level.dat")
 #initiate cat object

newUnit = unitClass.soldierClass()
newUnit.x= 400
newUnit.y=500
newUnit.id = 0

newUnit1 = unitClass.soldierClass()
newUnit1.x= 200
newUnit1.y=100
newUnit1.id = 1

while True:
    try:
        players[0].soldier.x = 200     
    except:
        print("failed")
    myserver.Pump()
    pygame.time.wait(50)
