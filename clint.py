from PodSixNet.Connection import ConnectionListener
import pygame

class MyClient(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        print(f"Trying to connect to {host}:{port}")

    def Network_connected(self, data):
        print("Connected to the server")
    
    def Network(self, data):
        # Handle incoming data from the server here
        pass



    def SendMove(self, direction):
        self.Send({"action": "move", "direction": direction})


myclient = MyClient("localhost", 1337)
while True:
    myclient.SendData({"message":"hello"})

    myclient.Pump()

    # ... rest of your game loop logic ...

    # Optionally, you can add a small delay to not overload the server
    # Especially important if you're sending data every loop iteration
    pygame.time.wait(50)  # wait for 50 milliseconds
