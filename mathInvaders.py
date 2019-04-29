import pygame
import math
import numpy as np
from random import *


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
answers =[]
Bullets =[]

class Bullet():
    vel = 5
    SIZE = 10
    
    def __init__(self, gameDisplay, pos):
        self.pos = pos
        self.visible = True
    def update(self):
        if (self.visible):
            self.pos[1] -= Bullet.vel
    def draw(self):
        if (self.visible):
            pygame.draw.circle(gameDisplay, black,self.pos, Bullet.SIZE) 

class ANS():
    # create static variable  for the speed
    #posXY = np.float64([0,0])
    #posXY = np.zeros((2))
    vel = 5
    SIZE = 50
    #self.posXY = np.array([0,0])
    posXY = np.array([0,0])

    def __init__(self, gameDisplay, posNum, text, row):
        #self.posXY = self.SIZE * posNum
        #self.posXY = np.array([0,0])
        x = display_width//4
        self.posXY = [ANS.SIZE + (x* posNum), ANS.SIZE+(2*ANS.SIZE*row)]
        print("self.posXY")
        print(self.posXY)
        self.text = text
        self.visible = True

    def update(self):
        if (self.visible):
            if ((self.posXY[0] <= 0 and ANS.vel <0) or (self.posXY[0] >= display_width and ANS.vel >0)):
                ANS.vel *= -1
            self.posXY[0] += ANS.vel

    def draw(self):
        if (self.visible):
            pygame.draw.circle(gameDisplay, black,self.posXY, ANS.SIZE) 
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render(str(self.text), 1, white)
            gameDisplay.blit(label, self.posXY)
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

def question(gameDisplay):
    size = 30
    rr =random()
    print(rr)
    rand = int(rr*3)
    print(rand)
    print("Adw")
    r1 = int(random()*10)
    r2 = int(random()*10)
    print("r1")
    print(r1)
    print("r2")
    print(r2)
    if ( rand == 0):
        ques = str(r1) + ' + ' + str(r2)
        ans = r1+r2
    elif (rand ==1):
        ques = str(r1) + ' - ' + str(r2)
        ans = r1-r2
    elif (rand ==2):
        ques = str(r1) + ' x ' + str(r2)
        ans = r1*r2
    #myfont = pygame.font.SysFont("monospace", size)
    #label = myfont.render(ques, 1, white)
    #gameDisplay.blit(label, [display_width/2 , 20])

    # if i wanna make the answers smart and not just one or two off i need to return the exact values
    #return r1, rand, r2, ans
    return ques, ans

print(question(gameDisplay))
print("^ANS")


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
    
def dist2D(x, y):
    return sqrt( ((x[1]-y[1])*(x[1]-y[1])) + ((x[0]-y[0])*(x[0]-y[0])) )


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
    shipPos = 1
    shipHeight =50
    shipWidth =50
    shipVel =25

    for i in range(4):
        a = ANS(gameDisplay, i, str(i),1)
        answers.append(a)
    for i in range(4):
        a = ANS(gameDisplay, i, str(i),3)
        answers.append(a)
    #for i in range(4):
        #print(answers[i].posXY)
        #print(answers[i].text)


    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.update()
        gameDisplay.fill(gray)
        btn(gameDisplay, startBtnPos, btnSize, green, "start", startClicked, mouse, click) 
        btn(gameDisplay, resetBtnPos, btnSize, green, "reset", resetClicked, mouse, click) 
        pygame.draw.rect(gameDisplay, green, [shipPos, display_height - shipHeight, shipWidth, shipHeight])
        #pygame.draw.rect(gameDisplay, color, [pos[0], pos[1], size[0], size[1]] )

        for i in Bullets:
            i.update()
            for ans in answers:
                if (ans.visible):
                    if(
            i.draw()
            if ( i.pos[1] < 0 or not i.visible ):
                Bullets.remove(i)
        #print(len(Bullets))

        for i in answers:
            i.update()
            i.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if ( shipPos > 0 ):
            if key[pygame.K_LEFT] :
                #moveLeft()
                shipPos -= shipVel
        if (shipPos < display_width-shipWidth):
            if key[pygame.K_RIGHT] :
                #moveRight()
                shipPos += shipVel

        if key[pygame.K_SPACE] :
            Bullets.append(Bullet(gameDisplay, [shipPos +(shipWidth//2), display_height - shipHeight]))
     
        #gameDisplay.blit(label, [0,0] )
    pygame.quit()
    quit()


gameLoop()

