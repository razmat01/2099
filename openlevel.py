import pygame



grassImage = pygame.image.load("assets/sprites/grass.png")
forestImage = pygame.image.load("assets/sprites/forest.png")
waterImage = pygame.image.load("assets/sprites/water.png")
catImage = pygame.image.load("assets/sprites/cat.png")

def openlevelfile(level):
    f = open(level,"r")

    x=0                       #FUNCTION TO TAKE FILENAME "LEVEL.DAT" AND RETURN LIST WITH ELEMENTS FOR EACH ROW.
    columns = []              #ROW ELEMENTS ARE LISTS WITH ELEMENTS OF CHARACTERS IN ROW

    while True:
        line = f.readline()
        row = []
        i=1
        for element in line:
            if(element != " "):
                row.append(element)
            i+=1 
        print(row)
        columns.append(row)
        if(row):
            print("e")
        else:
            break
    return columns

def drawLevel(scrn,level):
    y=0
    for element in level:
        x=0
        for element in element:
            if element == "G":
                scrn.blit(grassImage, (48*x,48*y))
            if element == "F":
                scrn.blit(forestImage, (48*x,48*y))
            if element == "W":
                scrn.blit(waterImage, (48*x,48*y))
            x+=1
        y+=1
    return scrn
