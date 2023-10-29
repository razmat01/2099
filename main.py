import pygame

pygame.init()

# Screen settings
scrn = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Displaying Cat Image')

# Load the image
imp = pygame.image.load("assets/sprites/cat.png")

# Image position variables
x = 0
y = 0
speed = 5  # Speed at which the image will move

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Get keys that are currently pressed down
    if keys[pygame.K_w]:  # W key
        y -= speed
    if keys[pygame.K_a]:  # A key
        x -= speed
    if keys[pygame.K_s]:  # S key
        y += speed
    if keys[pygame.K_d]:  # D key
        x += speed

    # Clear the screen
    scrn.fill((255, 255, 255))

    # Blit the image on every loop iteration
    scrn.blit(imp, (x, y))

    # Update the display
    pygame.display.flip()

pygame.quit()

