import pygame
import math
import numpy as np

pygame.init()

gray = (115, 115, 115)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

display_width = 800
display_height = 600

width = 10
height = width

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width, display_height))

FPS = 30
speed = 5
masses = []
G_constant =50
btnSize = [50 , 20]
startBtnPos = [display_width - btnSize[0] - 10, 10]
resetBtnPos = [ 10, 10]
gravityON = False

class Mass():
    posCentre = np.float64([0,0])
    vel = np.float64([0,0])
    accel = np.float64([0,0])
    size = 0
    color = (0,0,0)
    line = []
    startPos = []

    def __init__(self, gameDisplay, centreXY, size, color):
        self.startPos = centreXY
        self.posCentre = centreXY
        self.size = size
        self.color = color
        self.accel = np.float64([0,0])
        self.vel = np.float64([0,0])
        self.line = [] 
        #self.line[0] = self.posCentre
        #self.line.append(self.posCentre)
        self.line.append([self.posCentre[0], self.posCentre[1]])

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
        self.line.append([self.posCentre[0], self.posCentre[1]])
        #print(a)
        #print(self.vel)
        self.accel = np.float64([0,0])

    def draw(self, gameDisplay):
        a = self.posCentre 
        pygame.draw.circle(gameDisplay, self.color, a.astype(int) , self.size)
        pygame.draw.lines(gameDisplay, self.color, False, self.line, 1 )

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


def btn(gameDisplay, pos, size, color, txt, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #click = pygame.mouse.get_rel()
    #print(click)

    if (mouse[0] > pos[0] and mouse[0] < pos[0]+size[0]):
        if (mouse[1] > pos[1] and mouse[1] < pos[1]+size[1]):
            if (click[0] == 1):
                print("Awdaw")
                action()

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
    for a in masses:
        a.reset()
        a.update(gameDisplay)

def startClicked():
    global gravityON
    if (gravityON):
        gravityON = False
    else:
        gravityON = True

def gameLoop():
    gameDisplay.fill(gray)
    gameExit = False
    global gravityON

    ball = Mass(gameDisplay, [420,420], 50 , green) 
    masses.append(ball)
    sun = Mass(gameDisplay, [320,90], 90 , red) 
    masses.append(sun)
    moon = Mass(gameDisplay, [90,320], 30 , black) 
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

        pygame.display.update()
        gameDisplay.fill(gray)
        btn(gameDisplay, startBtnPos, btnSize, green, "start", startClicked) 
        btn(gameDisplay, resetBtnPos, btnSize, green, "reset", resetClicked) 


        if (gravityON):
            for a in range(len(masses)):
                for i in range(a):
                    #print([i,a])
                    gravityUpdate(masses[i], masses[a])

            for a in masses:
                a.update(gameDisplay)

        for a in masses:
            a.draw(gameDisplay)

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

