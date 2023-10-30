import pygame
from client import MyClient

class cat():
    x=0
    y=0
cat = cat()

pygame.init()
myclient = MyClient("localhost", 25565)
# Screen settings
scrn = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Displaying Cat Image')

# Load the image
imp = pygame.image.load("assets/sprites/cat.png")

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

    # Clear the screen
    scrn.fill((255, 255, 255))

    # Blit the image on every loop iteration
    scrn.blit(imp, (cat.x, cat.y))

    # Update the display
    pygame.display.flip()

pygame.quit()