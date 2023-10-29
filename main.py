import pygame

pygame.init()

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

    # Blit the image on every loop iteration
    scrn.blit(imp, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
