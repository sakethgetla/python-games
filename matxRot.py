import pygame
import math
import numpy as np


pygame.init()
gray = (115, 115, 115)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
lightGreen = (155, 255, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)

display_width = 1300
display_height = 900

width = 10
height = width

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))



def matxmul(x, y):
    #matx = np.ones
    # this should rotate pi/2 clockwise
    matx = [[1, -1],[1, 1]]
    np.multiply([x, y], matx)

    

def gameLoop():
    gameDisplay.fill(gray)
    gameExit = False
    while not gameExit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    pygame.quit()
    quit()
gameLoop()
