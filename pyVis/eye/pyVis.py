import matplotlib.pyplot as plt
#from PIL import Image
import cv2
import numpy as np
from PIL import Image

XOR = [
    [[0, 0], [0]],
    [[0, 1], [1]],
    [[1, 0], [1]],
    [[1, 1], [0]]
]

Hline = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
        ]
Vline = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
        ]


def toGrayscale(img):
    #print(img)  
    #print(type(img))  
    #print(len(img))  
    #print(len(img[0]))  
    width = len(img[0])
    height = len(img)

    # convert to grayscale
    a = np.zeros((height, width))
    print("convert to grayscale")
    for i in range(height):
        for j in range(width):
            #print(i)
            #print(j)
            a[i][j] = (img[i][j][0] + img[i][j][1] + img[i][j][2])/3

    return a




    #plt.imshow(a)
    #plt.imshow(a, cmap='gray', vmin=0, vmax=255)
    #plt.show()

# look at the differences between the two images
def imgDiff(img1, img2):
    print("runnung filter")  
    width = len(img1[0])
    height = len(img1)
    b = np.zeros((height, width))
    for i in range(height-2):
        for j in range(width-2):
            #print(i)
            #print(j)
            if (img1[i][j] != img2[i][j]):
                b[i][j] = img1[i][j] 
    return b




def filtering(img, mtx):
    print("runnung filter")  
    print(mtx)  
    width = len(img[0])
    height = len(img)
    b = np.zeros((height, width))
    for i in range(height-2):
        for j in range(width-2):
            #print(i)
            #print(j)
            b[i][j] = mtxMultiply(img, i, j, mtx)
    #plt.imshow(b, cmap='gray', vmin=0, vmax=255)
    #plt.show()
    return b

def mtxMultiply(img, i, j, mtx):
    val =0
    for y in range(len(mtx)):
        for x in range(len(mtx)):
            #print("(%d, %d)" %(x,y))
            val += img[i + y][j + x] * mtx[y][x]
            #print(" val (%d)" %(val))
    return val/3

def smoothen(img):
    #for grayscale
    print(img)  
    print(type(img))  
    print(len(img))  
    print(len(img[0]))  
    width = len(img[0])
    height = len(img)
    b = np.zeros((height, width))
    for i in range(height-2):
        for j in range(width-2):
            #print(i)
            #print(j)
            b[i+1][j+1] = normalize(avgAroundPix(img, i, j), 255)
    #plt.imshow(b, cmap='gray', vmin=0, vmax=255)
    #plt.show()
    return b

def avgAroundPix(a, x, y):
    return (a[x][y] + a[x+1][y] + a[x+2][y] + a[x][y+1] + a[x+1][y+1] + a[x+2][y+1] + a[x][y+2] + a[x+1][y+2] + a[x+2][y+2])/9
    #return (a[x][y] + a[x-1][y] + a[x-1][y+1] + a[x][y+1] + a[x+1][y+1] + a[x-1][y] + a[x+1][y-1] + a[x][y-1] + a[x-1][y-1])/9

def normalize(num, tot):
    return num/tot

    




img_file = 'eye.jpg'
img = cv2.imread(img_file, cv2.IMREAD_COLOR)    

a = toGrayscale(img)
grayScaleImg = Image.fromarray(a, 'L')
grayScaleImg.save('grayScaleImg.png')
grayScaleImg.show()
plt.imshow(a, cmap='gray', vmin=0, vmax=255)
#plt.show()
plt.savefig('grayScale.png')

#smoothend_image = Image.fromarray(smoothen(a), 'L')
#smoothend_image = Image.fromarray(smoothen(a), 'L')
#smoothend_image.save('smoothend_image.png')
#smoothend_image.show()

smoothenedImg = smoothen(a)
plt.imshow(smoothenedImg, cmap='gray', vmin=0, vmax=1)
plt.savefig('smoothenedImg.png')

doubleSmoothenedImg = smoothen(smoothenedImg)
plt.imshow(smoothenedImg, cmap='gray', vmin=0, vmax=1)
plt.savefig('doubleSmoothenedImg.png')


#filteredImage = filtering(a, Hline)
#plt.imshow( filteredImage, cmap='gray', vmin=0, vmax=255)
#plt.savefig('Hline.png')
#
#differenecesImg = imgDiff(filteredImage, a)
#plt.imshow( differenecesImg, cmap='gray', vmin=0, vmax=255)
#plt.savefig('diffImg.png')














#img_file = 'eye.jpg'
#img = cv2.imread(img_file, cv2.IMREAD_COLOR)    
#
#a = toGrayscale(img)
#plt.imshow(a, cmap='gray', vmin=0, vmax=255)
#plt.show()
#
#img_file = 'flower.jpeg'
#img = cv2.imread(img_file, cv2.IMREAD_COLOR)    
#
#a = toGrayscale(img)
#plt.imshow(a, cmap='gray', vmin=0, vmax=255)
#plt.show()








#im = Image.open('butterfly.jpg') # Can be many different formats.
#im = Image.open('butterfly.jpg', 'r')
#pix_val = list(im.getdata())

#pix_val is the list that contains all the pixel values which can be printed to see those values But the list got is a list of sets and some times its needed to flatten the list for example if the list is like: [(123,124,145,120), (345,453,234,124),……] and the list that is needed is [123, 124, 145, 120, 345, 453, 234, 124….] then the command to flatten the list is:
#pix_val_flat = [x for sets in pix_val for x in sets]

#print(pix_val)  # Get the RGBA Value of the a pixel of an image
#print(len(pix_val))  # Get the RGBA Value of the a pixel of an image
#print(len(pix_val[0]))  # Get the RGBA Value of the a pixel of an image


#plt.imshow(pix_val)
#plt.show()

#pix = im.load()
#print(im.size)  # Get the width and hight of the image for iterating over
#print(pix_val)  # Get the RGBA Value of the a pixel of an image
#pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#im.save('alive_parrot.png') 
