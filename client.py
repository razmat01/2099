from PodSixNet.Connection import ConnectionListener,connection
import pygame
import threading
import time
#asdasd
#client class . to be imported from main.py
#in charge of communications with server. 




class MyClient(ConnectionListener):
    x=0
    y=0
    def __init__(self, host, port):
        self.Connect((host, port)) #connect to the host server
        print(f"Trying to connect to {host}:{port}")
        self.Send({"action": "ping", "content": "ping"})

    def Network_message(self, data):
        print("Client message:", data['content'])

    def Network_connected(self,host): #connection message when succesfully connecting
        print("Connected to the server")
    
    def Network_return(self,host): #response from pinging server
        print("ping returned")

    def Network_catreturn(self,data):
        self.x = data["x"]
        self.y = data["y"]
    
    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def sendPing(self):
        self.Send({"action":"ping"})
        times = time.clock_gettime_ns()

    def sendData(self,message): #send message to server
        print("sended")
        print(message)
        self.Send(message)

    def SendMove(self, direction): #send movement to server
        self.Send({"action": "move", "direction": direction})

    def sendInput(self): #send custom message to server
        # Prompt the user for input
        message = input("Enter your message: ")

        self.sendData({"action":"message","content": message})




def pumping():
    connection.Pump()