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

pointSize = 50

width = 10
height = width

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
FPS = 30

class Point():
    touchedColor = black
    def __init__(self, gameDisplay, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color
    
    def changeColor(self, newColor):
        self.color = newColor

    def draw(self, gameDisplay):
        pygame.draw.circle(gameDisplay, self.color, self.pos, self.size)

def draw():
    pass

def gameLoop():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON
    nodes = []
    y = 0
    x = 0
    while (y < display_height):
        print("y , display_height")
        print(y, display_height)
        while (x < display_width):
            print("point")
            print(y , x)
            nodes.append(Point(gameDisplay, (x,y) , pointSize, blue))
            x += pointSize
        y += pointSize

    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for node in nodes:
            node.draw(gameDisplay)
        

        pygame.display.update()
        gameDisplay.fill(gray)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if key[pygame.K_q] :
            gameExit = True

    pygame.quit()
    quit()
gameLoop()
