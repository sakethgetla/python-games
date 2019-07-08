import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# 1 = nothing where as 2 showes the back camera ?

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # display in gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', gray)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



#import cv2

#import numpy as np
#
#cap = cv2.VideoCapture(0)
#while True:
#    ret.img = cap.read()
#    cv2.imshow('video output', img)
#    k=cv2.waitKey(10) & 0xff
#    if k==27:
#        break
#cap.release()
#cv2.destroyAllWindows()
