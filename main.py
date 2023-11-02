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




#levelArray = []
running = True




def network_pumping(): ##thread for inputs and network controls
    while True:  # Keep this running to continuously handle network operations
        
        myclient.Pump()
        client.pumping()
        myclient.sendData({"action":"updateRequest"})
        time.sleep(0.1)
        
levelArray=[]
network_thread = threading.Thread(target=network_pumping)
network_thread.start()
current_selected_soldier = None
current_unit_index = 0
while running:
    player_units = [unit for unit in client.allUnits if unit.attachedPlayer == myclient.player_number] #list of all units player owns

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Right mouse button
                if player_units:  # Check if there are any units
                    current_unit_index = (current_unit_index + 1) % len(player_units)  # Cycle to the next index
                    current_selected_soldier = player_units[current_unit_index] 
                    
            if event.button == 1:  # Left mouse button
                if current_selected_soldier:  # Only send if a soldier is selected
                    #print(current_selected_soldier)
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tile_x = (mouse_x - mapOffset["x"]) // zoom
                    tile_y = (mouse_y - mapOffset["y"]) // zoom
                    myclient.sendData({
                        "action": "move_soldier",
                        "id": current_selected_soldier.id,
                        "tile_x": tile_x, 
                        "tile_y": tile_y
                    })
                    current_selected_soldier.x = tile_x
                    current_selected_soldier.y = tile_y




    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # W key
        myclient.sendData({"action":"keypress","content":"W"})
    if keys[pygame.K_a]:  # A key
        myclient.sendData({"action":"keypress","content":"A"})
    if keys[pygame.K_s]:  # S key
            myclient.sendData({"action":"keypress","content":"S"})
    if keys[pygame.K_d]:  # D key
        myclient.sendData({"action":"keypress","content":"D"})
        #time.sleep(0.1)  # prevent the loop from running too fast

    if keys[pygame.K_l]:
        zoom+=zoom/40 #zoom in
    if keys[pygame.K_k]:
        zoom-=zoom/40 #zoom out
    if keys[pygame.K_UP]:
        mapOffset["y"] += 3#pan up
    if keys[pygame.K_DOWN]:
        mapOffset["y"] += -3 #pan down
    if keys[pygame.K_RIGHT]:
        mapOffset["x"] += -3 #pan right
    if keys[pygame.K_LEFT]:
        mapOffset["x"] += 3 # pan left
    


    if not levelArray:
        levelArray = openlevel.openlevelfile(myclient.level)


    scrn.fill((0, 0, 0))
    scrn = openlevel.drawLevel(scrn, levelArray, zoom, mapOffset)

    for unit in client.allUnits:
        scrn.blit(unit.imp, (unit.x * zoom + mapOffset["x"], unit.y * zoom + mapOffset["y"]))

    pygame.display.flip()


    clock.tick(60)

pygame.quit()