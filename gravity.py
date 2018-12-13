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

FPS = 30
speed = 5
masses = []
G_constant =90
btnSize = [50 , 20]
startBtnPos = [display_width - btnSize[0] - 10, 10]
resetBtnPos = [ 10, 10]
gravityON = False
startBtnClicked = False
line2vel_ratio = 0.1

class Mass():
    posCentre = np.float64([0,0])
    vel = np.float64([0,0])
    accel = np.float64([0,0])
    size = 0
    color = (0,0,0)
    line = []
    dotPos = []
    startPos = []
    clicked = False

    def __init__(self, gameDisplay, centreXY, size, color):
        self.startPos = centreXY
        self.posCentre = centreXY
        self.dotPos = centreXY
        self.size = size
        self.color = color
        self.accel = np.float64([0,0])
        self.vel = np.float64([0,0])
        self.line = [] 
        self.initVelLine = [] 
        #self.line[0] = self.posCentre
        #self.line.append(self.posCentre)
        self.line.append([self.posCentre[0], self.posCentre[1]])
        self.clicked = False

    def reset(self):
        self.posCentre = self.startPos
        self.vel = np.float64([0,0])
        self.accel = np.float64([0,0])
        self.line = []
        self.line.append([self.posCentre[0], self.posCentre[1]])

    def update(self, gameDisplay):
        #print("self.accel")
        #print(self.accel)
        #print("self.vel")
        #print(self.vel)
        self.vel += self.accel
        self.posCentre += self.vel
        a = self.posCentre.copy()
        self.dotPos = a.astype(int)
        self.line.append([self.posCentre[0], self.posCentre[1]])
        #print(a)
        #print(self.vel)
        self.accel = np.float64([0,0])


    def draw(self, gameDisplay, mouse, click):
        self.clicked = False
        a = self.posCentre.copy()
        pygame.draw.circle(gameDisplay, self.color, a.astype(int) , self.size)
        pygame.draw.lines(gameDisplay, blue, False, self.line, 1 )


        if not gravityON:
            if ( self.dotPos[0]-15 < mouse[0] < self.dotPos[0] + 15) and ( self.dotPos[1]-15 < mouse[1] < self.dotPos[1] + 15):
                if (click[0] == 1):
                    self.clicked = True
                   # mouse = pygame.mouse.get_pos()
                   # click = pygame.mouse.get_pressed()
                    self.dotPos = mouse

            if ( self.posCentre[0]-15 < mouse[0] < self.posCentre[0] + 15) and ( self.posCentre[1]-15 < mouse[1] < self.posCentre[1] + 15):
                if (click[2] == 1):
                    self.posCentre[0] = mouse[0]
                    self.posCentre[1] = mouse[1]
                    self.dotPos = mouse

        if self.clicked:
            pygame.draw.circle(gameDisplay, red, self.dotPos, 4)
        else :
            pygame.draw.circle(gameDisplay, black, self.dotPos, 4)

        pygame.draw.line(gameDisplay, white, self.dotPos, self.posCentre, 1)


def connect(XY1, XY2, w ):
    if (w < 0 ) :
        pygame.draw.line(gameDisplay, blue, XY2, XY1, int(round(w*2)*(-1)))
    else: 
        pygame.draw.line(gameDisplay, red, XY2, XY1, int(round(w*2)) )

    

#
#def gravityUpdate(obj1, obj2):
#    print("obj1.posCentre")
#    print(obj1.posCentre)
#    print("obj2.posCentre")
#    print(obj2.posCentre)
#    print(obj1.size)
#    relative_size = obj1.size/ obj2.size
#
#    distX = obj1.posCentre[0] - obj2.posCentre[0] 
#    distY = obj1.posCentre[1] - obj2.posCentre[1] 
#
#    dist = math.sqrt( math.pow(distX, 2) +  math.pow(distY, 2) )
#    print(dist)
#
#    a =  (obj2.size * G_constant ) /( dist**2)
#    print(a)
#
#    obj1.accel[0] += (distX/ dist)* a 
#    print(obj1.accel[0] )
#    obj1.accel[1] += (distY/ dist)* a 
#    print("obj1.accel")
#    print(obj1.accel)
#
#    b =  (obj1.size * G_constant ) /( dist**2)
#
#    obj2.accel[0] -= (distX/ dist)* b 
#    obj2.accel[1] -= (distY/ dist)* b 
#    print("obj2.accel")
#    print(obj2.accel)
#


def btn(gameDisplay, pos, size, color, txt, action, mouse, click):
    global startBtnClicked
    #click = pygame.mouse.get_rel()
    #print(click)
    click = pygame.mouse.get_pressed()

    if (click[0] == 1 and action != None ):
        if ( pos[0] < mouse[0] < pos[0]+size[0] and not startBtnClicked):
            if ( pos[1] < mouse[1] < pos[1]+size[1]):
                startBtnClicked = True
                action()
    else :
        startBtnClicked = False

    pygame.draw.rect(gameDisplay, color, [pos[0], pos[1], size[0], size[1]] )
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(str(txt), 1, black)
    gameDisplay.blit(label, pos)
    

def gravityUpdate(obj1, obj2):
    relative_size = obj1.size/ obj2.size

    distX = obj2.posCentre[0] - obj1.posCentre[0] 
    distY = obj2.posCentre[1] - obj1.posCentre[1] 

    dist = math.sqrt( math.pow(distX, 2) +  math.pow(distY, 2) )

    a =  (obj2.size * G_constant ) /( dist**2)

    obj1.accel[0] += (distX/ dist)* a
    obj1.accel[1] += (distY/ dist)* a

    b =  (obj1.size * G_constant ) /( dist**2)
    distX = obj1.posCentre[0] - obj2.posCentre[0] 
    distY = obj1.posCentre[1] - obj2.posCentre[1] 

    obj2.accel[0] += (distX/ dist)* b 
    obj2.accel[1] += (distY/ dist)* b 


def resetClicked():
    global gravityON
    gravityON = False
    for a in masses:
        a.reset()
        a.update(gameDisplay)

def startClicked():
    print("Awdaw")
    global gravityON
    if (gravityON):
        gravityON = False
    else:
        gravityON = True
        for a in masses:
            a.vel = (a.posCentre - a.dotPos) * line2vel_ratio

def gameLoop():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON

    sun = Mass(gameDisplay, [320,90], 150 , yellow) 
    masses.append(sun)
    ball = Mass(gameDisplay, [420,420], 40 , green) 
    masses.append(ball)
    moon = Mass(gameDisplay, [90,320], 15 , lightGreen) 
    masses.append(moon)
    moon = Mass(gameDisplay, [190,520], 15 , lightGreen) 
    masses.append(moon)

    for a in masses:
        a.update(gameDisplay)

    while not gameExit:
        #click = pygame.mouse.get_pressed()
        #print(click)
        #print(click[0])
        #masses[1].size +=1
        #masses[0].update(gameDisplay)
        #masses[1].update(gameDisplay)
        #masses[2].update(gameDisplay)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.update()
        gameDisplay.fill(gray)
        btn(gameDisplay, startBtnPos, btnSize, green, "start", startClicked, mouse, click) 
        btn(gameDisplay, resetBtnPos, btnSize, green, "reset", resetClicked, mouse, click) 


        if (gravityON):
            for a in range(len(masses)):
                for i in range(a):
                    #print([i,a])
                    gravityUpdate(masses[i], masses[a])

            for a in masses:
                a.update(gameDisplay)

        masses[0].posCentre[0] = display_width /2 
        masses[0].posCentre[1] = display_height/2 
        masses[0].dotPos = masses[0].posCentre.astype(int)

        for a in masses:
            a.draw(gameDisplay,  mouse, click)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if key[pygame.K_d] :
            masses[0].posCentre[0] += 1
        if key[pygame.K_q] :
            gameExit = True

     
        #gameDisplay.blit(label, [0,0] )
    pygame.quit()
    quit()


gameLoop()

