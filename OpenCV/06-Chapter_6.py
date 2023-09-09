# Reading a Video 

import cv2 as cv

cap = cv.VideoCapture("Resources/video.mp4")

# Indicator
if (cap.isOpened() == False):
    print("error in reading video")

# Reading and playing

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

