# How to capture a webcam inside python

# Step-1 import libraries
import cv2 as cv
import numpy as np

# Step-2 Read the frames from camera
cap = cv.VideoCapture(0) # webcam no.1
if (cap.isOpened() == False):
    print("There is an error")

# read untill the end
# Step-3 Display frame by frame
while(cap.isOpened()):
    #capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # To display frame
        cv.imshow("Frame", frame)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Step-4 Release or close windows easily
cap.release()
cv.destroyAllWindows()
