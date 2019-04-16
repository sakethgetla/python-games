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

class Bullet():
    self.pos = (0,0)
    self.vel = 5
    self.SIZE = 10
    
    def __init__(self, gameDisplay, pos):
        self.pos = pos
        

class ANS():
    # create static variable  for the speed

    self.posXY = (0,0)
    self.vel = 5
    self.SIZE = 50


    def __init__(self, gameDisplay, posXY, text):
        self.posXY = posXY
        self.text = text

    def update():
        self.pos.X += self.vel

    def draw():
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(self.text), 1, black)
        gameDisplay.blit(label, posXY)
         
    # check if the ans is hit


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


def btn(gameDisplay, pos, size,  color, txt, action, mouse, click):
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
    shipPos = 0
    shipHeight =50
    shipWidth =50

    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.update()
        gameDisplay.fill(gray)
        btn(gameDisplay, startBtnPos, btnSize, green, "start", startClicked, mouse, click) 
        btn(gameDisplay, resetBtnPos, btnSize, green, "reset", resetClicked, mouse, click) 
        pygame.draw.rect(gameDisplay, green, [shipPos, display_height - shipHeight], [shipWidth, shipHeight])




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

