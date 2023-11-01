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
imp = pygame.image.load("assets/sprites/cat.png")
zoom = 1

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

    for cat in client.cats:

        newCat = pygame.transform.scale_by(imp,0.1*zoom)
        scrn.blit(newCat, (cat.x*zoom+mapOffset["x"],cat.y*zoom+mapOffset["y"]))

    pygame.display.flip()

    clock.tick(60)
    #print(clock.get_fps())
    # Update the display
    

pygame.quit()