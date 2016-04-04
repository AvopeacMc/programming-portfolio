import pygame
import sys

from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Draw.py")

#colors
BLACK = (  0,  0,  0)
BLUE = (  0,  0, 255)
LTBLUE = (  6, 189, 247)
RED = (255,  0,  0)
GREEN = (  0, 255,  0)
WHITE = (255, 255, 255)
PURPLE = (148,  0, 211)
TURQ = ( 18, 255, 255)
MAJ = (225,  27, 197)
ORANGE = (255, 186,  0)
COPPER = (200, 117,  51)
TAN = (255, 222, 173)
BROWN = (130,  82,   1)
SILVER = (192, 192, 192)

DISPLAYSURF.fill(LTBLUE)
#pygame.draw.line(DISPLAYSURF, PURPLE, (0, 0), (400, 300), 4)
#pygame.draw.line(DISPLAYSURF, PURPLE, (0, 300), (400, 0), 4)
#pygame.draw.polygon(DISPLAYSURF, TURQ, ((200, 0), (250, 50), (225, 100), (175, 100), (150, 50)))
#pygame.draw.circle(DISPLAYSURF, MAJ, (200, 225), 50, 0)
#pygame.draw.ellipse(DISPLAYSURF, GREEN, (0, 100, 150, 100), 0)
#pygame.draw.rect(DISPLAYSURF, RED, (275, 112, 100, 75), 0)
#pygame.draw.rect(DISPLAYSURF, BLUE, (275, 200, 100, 75), 0)
#pygame.draw.polygon(DISPLAYSURF, ORANGE, ((175, 50), (225, 50) , (250, 100), (225, 150), (175, 150), (150, 100)))
pygame.draw.polygon(DISPLAYSURF, COPPER, ((200, 150), (250, 200), (150, 200)))
pygame.draw.rect(DISPLAYSURF, TAN, (150, 200, 100, 250), 0)
pygame.draw.rect(DISPLAYSURF, BROWN, (160, 250, 25, 50), 0)
pygame.draw.circle(DISPLAYSURF, BLACK, (165, 275), 2, 0)
pygame.draw.rect(DISPLAYSURF, SILVER, (210, 250, 30, 30), 0)
pygame.draw.line(DISPLAYSURF, BLACK, (211, 265), (239, 265), 1)
pygame.draw.line(DISPLAYSURF, BLACK, (225, 280), (225, 250), 1) 




while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
	