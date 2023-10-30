from PodSixNet.Connection import ConnectionListener,connection
import pygame
import threading
#asdasd
class MyClient(ConnectionListener):
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
        
    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def sendPing(self):
        self.Send({"action":"ping"})

    def sendData(self,message): #send message to server
        self.Send(message)

    def SendMove(self, direction): #send movement to server
        self.Send({"action": "move", "direction": direction})

    def sendInput(self): #send custom message to server
        # Prompt the user for input
        message = input("Enter your message: ")

        self.sendData({"action":"message","content": message})


myclient = MyClient("localhost", 25565)
while True:
    myclient.Pump()
    connection.Pump() #THIS ONE NECESSARY.
    x = threading.Thread(target=myclient.sendInput)
    x.start()

    #myclient.sendInput()
   # print("eee")

    pygame.time.wait(50)  # wait for 50 milliseconds