
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

pointSize = 30

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

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def gameLoop():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON
    nodes = []
    y = pointSize//2
    x = pointSize//2
    while (y < display_height):
        print("y , display_height")
        print(y, display_height)
        while (x < display_width):
            print("point")
            print(y , x)
            nodes.append(Point(gameDisplay, (x,y) ,  pointSize//2, blue))
            x += pointSize
        x = pointSize//2
        y += pointSize

    graph = np.zeros((len(nodes), len(nodes)))
    print(len(nodes))
    print(graph)

    gridWidth = display_width // pointSize
    gridHeight = dislaly_Height // pointSize

    for i in range(len(nodes)):
        if (i != 1):
            graph[i][i-1 - display_width] = 1      
            graph[i][i - display_width] = 1      
            graph[i][i+1 - display_width] = 1      
        if (y != 1):

        graph[i][i-1 + display_width] = 1      
        graph[i][i + display_width] = 1      
        graph[i][i+1 + display_width] = 1      

        graph[i][i-1] = 1      
        graph[i][i+1] = 1      

    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for node in nodes:
            if (click[0] == 1 and dist(node.pos, mouse) < pointSize):
                node.changeColor(black)
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
