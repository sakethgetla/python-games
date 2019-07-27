import math
import numpy as np


#gray = (115, 115, 115)
#black = (0, 0, 0)
#red = (255, 0, 0)
#blue = (0, 0, 255)
#green = (0, 255, 0)
#lightGreen = (155, 255, 0)
#yellow = (255, 255, 0)
#white = (255, 255, 255)

display_width = 1300
display_height = 900

width = 10
height = width


def make3D(pos_xyz):
    # at 0,0,0 





def matxmul(pos, rot):
    matx = [[np.cos(np.pi*rot*2), np.cos(np.pi*rot*2)], [1, 1]]
    pos = np.multiply(pos, matx)
    #pos = np.multiply(pos, matx)
    #pos = pos * matx
    print(pos)
    #matx = np.ones
    # this should rotate pi/2 clockwise

    

def gameLoop():
    pos_xyz = [10, 10, 10]
    pos_xy = [5, 1]
    matxmul(pos_xy, 1)

gameLoop()
