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

gridWidth = display_width // pointSize
gridHeight = display_height // pointSize

width = 10
height = width

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))
FPS = 30
findpath = False
btnWidth = 50
btnHeight = btnWidth//2


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

def btn(gameDisplay, pos, size, color, txt, action, mouse, click):
    # you can pass a pointer to a fuction as an argument while calling a fuction 
    # action is a fuction 
    global startBtnClicked
    #click = pygame.mouse.get_rel()
    #print(click)
    click = pygame.mouse.get_pressed()

    if (click[0] == 1 and action != None ):
        if ( pos[0] < mouse[0] < pos[0]+size[0] and not startBtnClicked):
            if ( pos[1] < mouse[1] < pos[1]+size[1]):
                startBtnClicked = True
                #calling the function that action is pointing to
                action()
    else :
        startBtnClicked = False

    pygame.draw.rect(gameDisplay, color, [pos[0], pos[1], size[0], size[1]] )
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(str(txt), 1, black)
    gameDisplay.blit(label, pos)


def startClicked():
    global findpath
    findpath = True

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_insideGrid(x, y):
    if ( x < gridWidth and y < gridHeight and x >= 0 and y >= 0):
        return True
    else :
        return False

def node2gridPos(num):
    return ((num%gridWidth)*pointSize, (num//gridWidth)*pointSize)

def gameLoop():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON
    nodes = []
    y = pointSize//2
    x = pointSize//2
    graphWidth = 0
    graphHeight = 0
    while (y < display_height):
        print("y , display_height")
        print(y, display_height)
        graphHeight += 1
        while (x < display_width):
            graphWidth += 1
            print("point")
            print(y , x)
            nodes.append(Point(gameDisplay, (x,y) ,  pointSize//2, blue))
            x += pointSize
        x = pointSize//2
        y += pointSize

    graph = []
    for j in range(gridHeight):
        assert(j < gridHeight)
        for i in range(gridWidth):
            connections = []

            for px in range(-1, 2):
                for py in range(-1, 2):
                    print("awdwad")
                    print(px, py)
                    pos = (i+px, j+py)
                    if (is_insideGrid(pos[0], pos[1]) and not (px ==0 and py == 0) ):
                        connections.append(pos[0] + (pos[1]*gridWidth))
            graph.append(connections)

    print("graph")
    print(len(graph))
    print(graph)
    print(gridWidth)
    print(graph[gridWidth])
    counter = 0

    visited = np.empty((len(graph)))
    path = np.empty((len(graph)))
    print(type(visited))
    print(len(visited))
    
    gameExit = True
    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for node in nodes:
            if (click[0] == 1 and dist(node.pos, mouse) < pointSize//2):
                node.changeColor(black)
            #else :
            #    node.changeColor(blue)
            node.draw(gameDisplay)


        #if (counter < len(nodes)):
        #    nodes[counter].changeColor(black)
        #    nodes[counter].draw(gameDisplay)
        #    for i in graph[counter] :
        #        nodes[i].changeColor(green)
        #        nodes[i].draw(gameDisplay)
        #counter += 1
        btn(gameDisplay, (display_width-btnWidth -5, btnHeight), (btnWidth, btnHeight), yellow, "start", startClicked, mouse, click)

        global findpath
        if(findpath):
            print("clicked")
             

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
