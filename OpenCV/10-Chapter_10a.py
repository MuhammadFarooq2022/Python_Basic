# Convert in to different shades of Gray and Black & White
# Step-1 import libraries
import cv2 as cv
import numpy as np

# Step-2 Read the frames from camera
cap = cv.VideoCapture(0) # webcam no.1

while(True):
    #capture frame by frame
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)
    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("BinaryCam", binary)
    # To quit with q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv.destroyAllWindows()
