import pygame
import openlevel
import client
import time



pygame.init()
myclient = client.MyClient("localhost", 25565)
# Screen settings
scrn = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption('Displaying Cat Image')

# Load the image
imp = pygame.image.load("assets/sprites/cat.png")
myclient.sendData({"action":"requestMap"})
time.sleep(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()  # Get keys that are currently pressed down
    if keys[pygame.K_w]:  # W key
        myclient.sendData({"action":"keypress","content":"W"})
    if keys[pygame.K_a]:  # A key
        print("A")
        myclient.sendData({"action":"keypress","content":"A"})
    if keys[pygame.K_s]:  # S key
        myclient.sendData({"action":"keypress","content":"S"})
    if keys[pygame.K_d]:  # D key
        myclient.sendData({"action":"keypress","content":"D"})
    
    #myclient.pumping()
    

    # Clear the screen
    myclient.sendData({"action":"updateRequest"})
    scrn.fill((255, 255, 255))
    myclient.Pump()
    client.pumping()
    # Blit the image on every loop iteration

    scrn = openlevel.drawLevel(scrn,myclient.level)
    scrn.blit(imp, (myclient.x,myclient.y))

    # Update the display
    pygame.display.flip()

pygame.quit()