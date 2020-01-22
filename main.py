import pygame
from random import *
import datetime
from itertools import product, starmap

# These constants define our platform types:
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

LEFTBUFFER = 30
TOPBUFFER = 45
XBUFFER = (23 + 75) * 0

GRAVEL                = (31 + XBUFFER, 47, 75, 75)
IRON                  = (31 + XBUFFER, 138, 75, 75)
GEM                   = (31 + XBUFFER, 230, 75, 75)
COMBINE               = (31 + XBUFFER, 321, 75, 75)
DIAMOND               = (31 + XBUFFER, 413, 75, 75)
GOLD                  = (31 + XBUFFER, 504, 75, 75)

selection = [GRAVEL,IRON,GEM,COMBINE,DIAMOND,GOLD]

Topspace = 150
tileheight = 10
tilewidth = 4

def checkNeighbors(y,x):
    if y == 0:
        return True
    else:
        if(tileMapIndex[y-1][x] == -1):
            return True
        else:
            return False

def makeNewTile():
    index = randint(0,5)
    xindex = randint(0,tilewidth - 1)
    yindex = randint(0,tileheight - 1)
    if(tileMapIndex[yindex][xindex] == -1) and ((yindex == tileheight - 1) or tileMapIndex[yindex+1][xindex] != -1):
        tileMap[yindex][xindex] = tileImages[index]
        tileMapIndex[yindex][xindex] = index
    return

def draw():
    screen.fill(background_colour)
    for i, layer in enumerate(tileMap):
        for j, tile in enumerate(layer):
            if(tile != -1):
                screen.blit(tile, (j * 75, Topspace + (75 * i)))
            pass
        pass
    pygame.display.flip()

def checkClick(pos):
    xpos = int(pos[0] / 75)
    ypos = int((pos[1] / 75) - (Topspace / 75))
    # print(tileMapIndex[ypos][xpos])
    if checkNeighbors(ypos,xpos):
        tileMapIndex[ypos][xpos] = -1
        tileMap[ypos][xpos] = -1
    print(tileMapIndex)

    return

def get_image(sprite_sheet, x, y, width, height):
    # Create a new blank image
    image = pygame.Surface([width, height]).convert()

    # Copy the sprite from the large sheet onto the smaller image
    image.blit(sprite_sheet, (0, 0), (x, y, width, height))

    # Assuming black works as the transparent color
    image.set_colorkey((0,0,0))

    # Return the image
    return image

pygame.init()

background_colour = (0,0,0)
(width, height) = (300, 900)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Literally Just Bricks')
screen.fill(background_colour)

sprite_sheet = pygame.image.load("tiles.jpg").convert()

tileImages = []
for i in range(6):
    tileImages.append(get_image(sprite_sheet, selection[i][0], selection[i][1], selection[i][2], selection[i][3]))

tileMap = []
tileMapIndex = []
for i in range(tileheight):
    mapLayer = []
    mapLayerIndex = []
    for j in range(tilewidth):
        index = randint(0,5)
        mapLayer.append(tileImages[index])
        mapLayerIndex.append(index)
    tileMap.append(mapLayer)
    tileMapIndex.append(mapLayerIndex)

for i, layer in enumerate(tileMap):
    for j, tile in enumerate(layer):
        screen.blit(tile, (j * 75, Topspace + (75 * i)))
        pass
    pass

pygame.display.flip()

running = True
lasttime = datetime.datetime.now()
currtime = datetime.datetime.now()
while running:
    currtime = datetime.datetime.now()
    if randint(0, 100) < 100 and (currtime - lasttime).total_seconds() > .05:
        makeNewTile()
        draw()
        lasttime = datetime.datetime.now()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
        # if pygame.mouse.get_pressed()[0]:
            coords = pygame.mouse.get_pos()
            checkClick(coords)
            draw()
        if event.type == pygame.QUIT:
            running = False
