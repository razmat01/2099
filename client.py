from PodSixNet.Connection import ConnectionListener,connection
import pygame
import threading
import time
import openlevel

cats = []
class catClass():
    x=0
    y=0

class MyClient(ConnectionListener):


    level = "level.dat"
    def __init__(self, host, port):
        self.Connect((host, port)) #connect to the host server
        print(f"Trying to connect to {host}:{port}")
        self.Send({"action": "ping", "content": "ping"})
    
    def Network_updateRequest(self,data):

        x=data["x"]
        y=data["y"]

    def Network_message(self, data):
        print("Client message:", data['content'])

    def Network_connected(self,host): #connection message when succesfully connecting
        print("Connected to the server")
    
    def Network_return(self,host): #response from pinging server
        print("ping returned")

    def Network_catreturn(self,data):
        #cats = []
        for i in range(data["i"]):
            dummycat = catClass
            dummycat.x=data["x"]
            dummycat.y=data["y"]
            cats.append(dummycat)
            

    def sendPing(self):
        self.Send({"action":"ping"})
        times = time.clock_gettime_ns()

    def sendData(self,message): #send message to server


        self.Send(message)
    
    def Network_mapReturn(self,data):
        level = data["content"]
        print(level, "     e")
        #openlevel.drawLevel(main.scrn,data["content"])

    def SendMove(self, direction): #send movement to server
        self.Send({"action": "move", "direction": direction})

    def sendInput(self): #send custom message to server
        # Prompt the user for input
        message = input("Enter your message: ")

        self.sendData({"action":"message","content": message})

def pumping():
    connection.Pump()