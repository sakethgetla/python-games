
#import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # display in gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray)

    # Display the resulting frame
    #print(frame)
    #print(np.shape(frame))
    #print(type(frame))
    #print(ret)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(gray)
    #print(np.shape(gray))
    #edges = np.zeros_like(gray)
    #e = np.zeros((10,2), int)
    #print(e)
    #b = []
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #edges = cv2.goodFeaturesToTrack(gray, max_corners, quality_lev, min_dist)
    ##edges = cv2.Canny(frame, edges)
    ##edges = cv2.canny(frame, edges, 10, 30)
    ##print(gray)
    #print(edges)
    #print(np.shape(gray))
    cv2.imshow('frame', frame)
    #cv2.imshow('frame', frame)
    #break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

