from PodSixNet.Connection import ConnectionListener
import pygame

class MyClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        print(f"Trying to connect to {host}:{port}")

    def Network_connected(self, data):
        print("Connected to the server")
    
    def sendInput(self):
        # Prompt the user for input
        message = input("Enter your message: ")
        self.sendData({"message": message})
    
    def Network(self, data):
        # Handle incoming data from the server here
        pass

    def sendData(self,message):
        self.Send(message)

    def SendMove(self, direction):
        self.Send({"action": "move", "direction": direction})


myclient = MyClient("localhost", 25565)
while True:
    # Send the user's input to the server
    myclient.sendInput()

    myclient.Pump()

    # Optionally, you can add a small delay to not overload the server
    pygame.time.wait(50)  # wait for 50 milliseconds