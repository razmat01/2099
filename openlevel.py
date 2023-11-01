import pygame



grassImage = pygame.image.load("assets/sprites/grass.png")
forestImage = pygame.image.load("assets/sprites/forest.png")
waterImage = pygame.image.load("assets/sprites/water.png")
catImage = pygame.image.load("assets/sprites/cat.png")

def openlevelfile(level):
    f = open(level,"r")
    print("test1")
    x=0                       #FUNCTION TO TAKE FILENAME "LEVEL.DAT" AND RETURN LIST WITH ELEMENTS FOR EACH ROW.
    columns = []              #ROW ELEMENTS ARE LISTS WITH ELEMENTS OF CHARACTERS IN ROW

    while True:
        print("test2 column ", x)
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

def drawLevel(scrn,level,zoom,mapOffset = {"x":0,"y":0}):
    y=0
    for element in level:
        x=0
        for element in element:
            if(10 < (48*x*zoom+mapOffset["x"])<1900 and (10 < 48*y*zoom+mapOffset["y"]<1000)):
                if element == "G":
                    newGrass = pygame.transform.scale_by(grassImage,zoom)
                    scrn.blit(newGrass, (48*x*zoom+mapOffset["x"],48*y*zoom+mapOffset["y"]))
                if element == "F":
                    newForest = pygame.transform.scale_by(forestImage,zoom)
                    scrn.blit(newForest, (48*x*zoom+mapOffset["x"],48*y*zoom+mapOffset["y"]))
                if element == "W":
                    newWater = pygame.transform.scale_by(waterImage,zoom)
                    scrn.blit(newWater, (48*x*zoom+mapOffset["x"],48*y*zoom+mapOffset["y"]))
            x+=1
        y+=1
    return scrn


