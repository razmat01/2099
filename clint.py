from PodSixNet.Connection import ConnectionListener,connection
import pygame
#asdasd
class MyClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        print(f"Trying to connect to {host}:{port}")

    def Network_connected(self, data):
        print("Connected to the server")
    
    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def sendData(self,message):
        self.Send(message)

    def SendMove(self, direction):
        self.Send({"action": "move", "direction": direction})

    def sendInput(self):
        # Prompt the user for input
        message = input("Enter your message: ")
        connection.send({"action":"message","content": message})
        self.sendData({"action":"message","content": message})


myclient = MyClient("localhost", 25565)
while True:
    
    myclient.Pump()
    connection.Pump()
    print("gimp")
    myclient.sendData({"action":"message","content":"hello"})
    #myclient.sendInput()
   
    pygame.time.wait(50)  # wait for 50 milliseconds