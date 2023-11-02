from PodSixNet.Connection import ConnectionListener,connection
import pygame
from threading import Lock
import time
import openlevel

allUnits_lock = Lock()
SOLDIER_IMAGE = pygame.image.load("assets/sprites/placeholder1.png")
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
        self.attachedPlayer = None
        self.imp = SOLDIER_IMAGE



cats = []
class catClass():
    x=0
    y=0

class MyClient(ConnectionListener):
    def Network_add_new_soldier(self, data):
        with allUnits_lock:  # acquire lock before modifying allUnits
            # create a new soldier instance using the provided data
            soldier = soldierClass()
            soldier.id = data["id"]
            soldier.type = data["type"]
            soldier.x = data["x"]
            soldier.y = data["y"]
            soldier.attachedPlayer = data["player"]
            # Append the new soldier to the allUnits list
            print(soldier, "  soldier")


    level = "level.dat"
    def __init__(self, host, port):
        self.Connect((host, port)) #connect to the host server
        self.player_number=None
        print(f"Trying to connect to {host}:{port}")
        self.Send({"action": "ping", "content": "ping"})
    
    def Network_updateRequest(self,data):

        x=data["x"]
        y=data["y"]
    def Network_updateReturn(self, data):
        with allUnits_lock:  # acquire lock before modifying allUnits
            # find the soldier and update its position
            unit = next((u for u in allUnits if u.id == data["id"]), None)
            if not unit:
                unit = soldierClass()
                allUnits.append(unit)

            unit.x = data["x"]
            unit.y = data["y"]

            

    def Network_message(self, data):
        print("Client message:", data['content'])

    def Network_connected(self,host): #connection message when succesfully connecting
        print("Connected to the server")
    
    def Network_assign_player_number(self, data):
        self.player_number = data["player_number"]
        print(f"Assigned player number: {self.player_number}")
        
    def Network_return(self,host): #response from pinging server
        print("ping returned")


    def sendPing(self):
        self.Send({"action":"ping"})
        times = time.clock_gettime_ns()

    def sendData(self,message): #send message to server


        self.Send(message)
    
    def Network_mapReturn(self,data):
        level = data["content"]
       
        #openlevel.drawLevel(main.scrn,data["content"])

    def SendMove(self, direction): #send movement to server
        self.Send({"action": "move", "direction": direction})

    def sendInput(self): #send custom message to server
        # Prompt the user for input
        message = input("Enter your message: ")

        self.sendData({"action":"message","content": message})

def pumping():
    connection.Pump()
    time.sleep(0.05)