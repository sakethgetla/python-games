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
pos_xy = [10, 10]
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
FPS = 30



def matxmul(pos, rot):
    #matx = np.ones
    # this should rotate pi/2 clockwise
    matx = [[1, -1],[1, 1]]
    np.multiply([x, y], matx)

def rotate(pos, screenCentre, rot):
    pos[0] = (pos[0]/math.sqrt(((pos[0])*(pos[0])) + ((pos[1])*(pos[1])))
    #pos[0] = math.sin(math.pi * rot[0]) + math.cos(math.pi * rot[0])
    #pos[1] = -math.cos(math.pi * rot[0]) + math.sin(math.pi * rot[0])
    #pos[0] = math.sin(math.pi * rot)
    rot = [0, 0, 0]

def display2Screen(gameDisplay):


def gameLoop():
    gameDisplay.fill(gray)
    gameExit = False

    pos = [50, 50, 50]
    size = [150, 150, 150]
    rot = 0.0

    
    while not gameExit:
        #print("adwaw")
        pygame.display.update()
        gameDisplay.fill(gray)
        
        pygame.draw.rect(gameDisplay, red, [pos[0], pos[1], size[0], size[1]] )

        key = pygame.key.get_pressed()
        if (key[pygame.K_LEFT] or key[pygame.K_a]) :
            rot[0] += 0.1
            rotate(pos, size, rot)

        #click = pygame.mouse.get_pressed()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
    pygame.quit()
    quit()
gameLoop()
