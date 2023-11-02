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

class soldierClass(unitClass):
    def __init__(self):
        super().__init__()
        self.id = len(allUnits)
        self.type = "soldier"
        self.movement = 3
        self.x = 0
        self.y = 0
        self.attachedPlayer = 1

class terrainClass():
    pass

class forestClass(terrainClass):
    def __init__(self):
        super().__init__()
        self.type = "forest"
        self.x = 0
        self.y = 0

class playerClass():
    soldiers = []

    address = ""
    channel = ""
    player_number = None  # New attribute to store the player number

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

        for i in range(len(allUnits)):
            self.Send({"action":"updateReturn","type":allUnits[i].type,"player":allUnits[i].attachedPlayer,"x":allUnits[i].x,"y":allUnits[i].y,"id":allUnits[i].id})
        
    def Network_requestMap(self,data):

        self.Send({"action":"mapReturn","content":"level.dat"})
    def Network_move_soldier(self, data):
        # Identify the soldier by its ID
        soldier = next((u for u in allUnits if u.id == data["id"]), None)
        
        if soldier:
            # Update the soldier's position
            soldier.x = data['tile_x'] - (data['tile_x']%48)
            soldier.y = data['tile_y'] - (data['tile_y']%48)
            
            # Inform all clients about the new position
            for player in players:
                #player.channel.Send({"action": "update_soldier_position", "id": soldier.id, "x": soldier.x, "y": soldier.y})
                for i in range(len(allUnits)):
                    self.Send({"action":"updateReturn","type":allUnits[i].type,"player":allUnits[i].attachedPlayer,"x":allUnits[i].x,"y":allUnits[i].y,"id":allUnits[i].id})

        
  
class MyServer(Server):
    channelClass = ClientChannel
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)
        self.next_player_number = 0

    def Connected(self, channel, addr):
        print("New connection from address:", addr)
        print("New connection:", channel)
        new_player = playerClass()
        new_player.player_number = self.next_player_number
        self.next_player_number += 1

        new_player.address = addr
        new_player.channel = channel
        players.append(new_player)

        # Send the unique player number to the client
        channel.Send({"action": "assign_player_number", "player_number": new_player.player_number})
        sleep(0.5)
        initialize_soldier_for_player(new_player.player_number)

def create_soldier(player_number):
    soldier = soldierClass()
    soldier.x, soldier.y = 300, 700
    soldier.attachedPlayer = player_number
    return soldier

players = []
myserver = MyServer(localaddr=("0.0.0.0", 25565))

print("server listening")
level = openlevel.openlevelfile("level.dat")
 #initiate cat object

def initialize_soldier_for_player(player_number):
    player = next((p for p in players if p.player_number == player_number), None)
    if player is None:
        print(f"No player found with player number {player_number}")
        return

    for i in range(2):  # initialize two soldiers
        soldier = create_soldier(player_number)
        allUnits.append(soldier)
        player.soldiers.append(soldier)
        # notify all clients about the new soldier
        for other_player in players:
            other_player.channel.Send({
                "action": "add_new_soldier",
                "type": soldier.type,
                "player": soldier.attachedPlayer,
                "x": soldier.x,
                "y": soldier.y,
                "id": soldier.id
            })
    

while True:
    myserver.Pump()
    print(allUnits)
    pygame.time.wait(500)
