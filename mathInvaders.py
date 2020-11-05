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
    vel = 25
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
    SIZE = 30
    #self.posXY = np.array([0,0])
    posXY = np.array([0,0])
    distBetweenAns = display_width//7

    def __init__(self, gameDisplay, startPos, posNum, text, row):
        #self.posXY = self.SIZE * posNum
        #self.posXY = np.array([0,0])
        self.posXY = [ANS.SIZE +startPos+ (ANS.distBetweenAns* posNum), ANS.SIZE+(2*ANS.SIZE*row)]
        #print("self.posXY")
        #print(self.posXY)
        self.text = text
        self.visible = True

    def update(self):
        if (self.visible):
            self.posXY[0] += ANS.vel

    def draw(self):
        if (self.visible):
            pygame.draw.circle(gameDisplay, black,self.posXY, ANS.SIZE) 
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render(str(self.text), 1, white)
            if (self.text < 0 or self.text > 9):
                #ans only has one charater including negative sign (-)
                gameDisplay.blit(label, [self.posXY[0]- (ANS.SIZE//2), self.posXY[1]- (ANS.SIZE//2)])
            else :
                gameDisplay.blit(label, [self.posXY[0]- (ANS.SIZE//4), self.posXY[1]- (ANS.SIZE//2)])

                    
        # check if the ans is hit


def connect(XY1, XY2, w ):
    if (w < 0 ) :
        pygame.draw.line(gameDisplay, blue, XY2, XY1, int(round(w*2)*(-1)))
    else: 
        pygame.draw.line(gameDisplay, red, XY2, XY1, int(round(w*2)) )

def ansVisible(answers):
    for ans in answers:
        if(ans.visible):
            return True
    return False
    


#def gravityUpdate(obj1, obj2):
    #print("obj1.posCentre")
    #print(obj1.posCentre)
    #print("obj2.posCentre")
    #print(obj2.posCentre)
    #print(obj1.size)
    #relative_size = obj1.size/ obj2.size

    #distX = obj1.posCentre[0] - obj2.posCentre[0] 
    #distY = obj1.posCentre[1] - obj2.posCentre[1] 

    #dist = math.sqrt( math.pow(distX, 2) +  math.pow(distY, 2) )
    #print(dist)

    #a =  (obj2.size * G_constant ) /( dist**2)
    #print(a)

    #obj1.accel[0] += (distX/ dist)* a 
    #print(obj1.accel[0] )
    #obj1.accel[1] += (distY/ dist)* a 
    #print("obj1.accel")
    #print(obj1.accel)

    #b =  (obj1.size * G_constant ) /( dist**2)

    #obj2.accel[0] -= (distX/ dist)* b 
    #obj2.accel[1] -= (distY/ dist)* b 
    #print("obj2.accel")
    #print(obj2.accel)


def newQuestion(gameDisplay, answers):
    size = 30
    rr =random()
    # if correctAnsNo is not visible this does not work
    #correctAnsNo = int(random()*len(answers))
    # counter counter the number of answers that are visible
    counter = 0
    rand = int(rr*3)
    r1 = int(random()*10)
    r2 = int(random()*10)
    found = False
    randCorrectAns = int(random()*len(answers))
    #print(rr)
    #print(rand)
    #print("Adw")
    #print("r1")
    #print(r1)
    #print("r2")
    #print(r2)
    if ( rand == 0):
        ques = str(r1) + ' + ' + str(r2)
        correctAns = r1+r2
    elif (rand ==1):
        ques = str(r1) + ' - ' + str(r2)
        correctAns = r1-r2
    elif (rand ==2):
        ques = str(r1) + ' x ' + str(r2)
        correctAns = r1*r2


    for ans in answers:
        if (ans.visible):
            randAns = random()
            # range from -5 to 5 including 0 
            randAns *= 11
            randAns -= 5
            randAns = int(randAns)
            ans.text = randAns + correctAns

    while(not found):
        for ans in answers:
            if( ans.visible ):
                if ( counter == randCorrectAns):
                    found = True
                    ans.text = correctAns
                counter += 1



    #myfont = pygame.font.SysFont("monospace", size)
    #label = myfont.render(ques, 1, white)
    #gameDisplay.blit(label, [display_width/2 , 20])

    # if i wanna make the answers smart and not just one or two off i need to return the exact values
    #return r1, rand, r2, ans
    return ques, correctAns

#print(question(gameDisplay))
#print("^ANS")


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
    return math.sqrt( ((x[1]-y[1])*(x[1]-y[1])) + ((x[0]-y[0])*(x[0]-y[0])) )


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
    question = ""
    correctAns = 10
    changeVel = False



    # create a class for each row of the answers
    # make each row have a seperate vel


    start = 2 * ANS.distBetweenAns//3
    for i in range(4):
        a = ANS(gameDisplay,start, i, str(i),1)
        answers.append(a)
    start = ANS.distBetweenAns//3
    for i in range(5):
        a = ANS(gameDisplay,start, i, str(i),3)
        answers.append(a)
    start = 0
    for i in range(6):
        a = ANS(gameDisplay,start, i, str(i),5)
        answers.append(a)
    #for i in range(4):
        #print(answers[i].posXY)
        #print(answers[i].text)
        question, correctAns = newQuestion(gameDisplay, answers)


    while not gameExit:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.update()
        gameDisplay.fill(gray)
        #btn(gameDisplay, startBtnPos, btnSize, green, "start", startClicked, mouse, click) 
        #btn(gameDisplay, resetBtnPos, btnSize, green, "reset", resetClicked, mouse, click) 
        pygame.draw.rect(gameDisplay, green, [shipPos, display_height - shipHeight, shipWidth, shipHeight])
        #pygame.draw.rect(gameDisplay, color, [pos[0], pos[1], size[0], size[1]] )
        removeBullet = False

        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render(question, 1, white)
        gameDisplay.blit(label, [display_width/2 , 20])

        for b in Bullets:
            b.update()
            for ans in answers:
                if(ans.visible and ANS.SIZE + Bullet.SIZE > dist2D(b.pos, ans.posXY)):
                    # ans collision with b and ans is visible
                    removeBullet = True
                    if (correctAns == ans.text):
                        ans.visible = False
                        if (ansVisible(answers)):
                            question, correctAns = newQuestion(gameDisplay, answers)
                        #else :
                        #    # all ans not visible
                        #    gameExit = True
            b.draw()
            if ( b.pos[1] < 0 or not b.visible ):
                removeBullet = True
            if(removeBullet):
                removeBullet = False
                Bullets.remove(b)

        #print(len(Bullets))

        for i in answers:
            if (i.visible):
                if ((i.posXY[0] <= 0 and ANS.vel <0) or (i.posXY[0] >= display_width and ANS.vel >0)):
                    changeVel = True

            i.update()
            i.draw()
        if (changeVel):
            ANS.vel *= (-1)
            changeVel = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        clock.tick(FPS)
        key = pygame.key.get_pressed()
        if ( shipPos > 0 ):
            if (key[pygame.K_LEFT] or key[pygame.K_a]) :
                #moveLeft()
                shipPos -= shipVel
        if (shipPos < display_width-shipWidth):
            if (key[pygame.K_RIGHT] or key[pygame.K_d]):
                #moveRight()
                shipPos += shipVel

        if key[pygame.K_SPACE] :
            Bullets.append(Bullet(gameDisplay, [shipPos +(shipWidth//2), display_height - shipHeight]))
     
        if key[pygame.K_q] :
            gameExit = True
        #gameDisplay.blit(label, [0,0] )

    pygame.quit()
    quit()


gameLoop()

