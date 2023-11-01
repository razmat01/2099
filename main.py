import pygame
import openlevel
import client
import time
import threading

clock = pygame.time.Clock()
mapOffset = {"x":0,"y":0}
pygame.init()
myclient = client.MyClient("localhost", 25565)
# Screen settings
scrn = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption('Displaying Cat Image')

# Load the image
imp = pygame.image.load("assets/sprites/placeholder1.png")
zoom = 1

unitdummy = client.unitClass.soldierClass()
unitdummy.x = 100
unitdummy.y = 400
unitdummy.type = "soldier"
unitdummy.attachedPlayer = 0
client.allUnits.append(unitdummy)

unitdummy2 = client.unitClass.soldierClass()
unitdummy2.x = 300
unitdummy2.y = 700
unitdummy2.type = "soldier"
unitdummy2.attachedPlayer = 0
client.allUnits.append(unitdummy2)


levelArray = []
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(levelArray==[]):
        levelArray = openlevel.openlevelfile(myclient.level)
    

    keys = pygame.key.get_pressed()  # Get keys that are currently pressed down
    if keys[pygame.K_w]:  # W key
        myclient.sendData({"action":"keypress","content":"W"})
    if keys[pygame.K_a]:  # A key
        myclient.sendData({"action":"keypress","content":"A"})
    if keys[pygame.K_s]:  # S key
        myclient.sendData({"action":"keypress","content":"S"})
    if keys[pygame.K_d]:  # D key
        myclient.sendData({"action":"keypress","content":"D"})
    if keys[pygame.K_l]:
        zoom+=zoom/20 #zoom in
    if keys[pygame.K_k]:
        zoom-=zoom/20 #zoom out
    if keys[pygame.K_UP]:
        mapOffset["y"] += 3#pan up
    if keys[pygame.K_DOWN]:
        mapOffset["y"] += -3 #pan down
    if keys[pygame.K_RIGHT]:
        mapOffset["x"] += -3 #pan right
    if keys[pygame.K_LEFT]:
        mapOffset["x"] += 3 # pan left
    

    

    # Clear the screen
    myclient.sendData({"action":"updateRequest"})

    scrn.fill((0, 0, 0))
    myclient.Pump()
    client.pumping()

    scrn = openlevel.drawLevel(scrn,levelArray,zoom,mapOffset)

    i=0
    for i in range(len(client.allUnits)):
        print(client.allUnits[i])
        scrn.blit(client.allUnits[i].imp,(client.allUnits[i].x*zoom+mapOffset["x"],client.allUnits[i].y*zoom+mapOffset["y"]))
        time.sleep(0.02)



    pygame.display.flip()

    clock.tick(60)
    #print(clock.get_fps())
    # Update the display
    

pygame.quit()