# Converting Video to gray or Black and White 

import cv2 as cv

cap = cv.VideoCapture("Resources/video.mp4")

# Reading and playing

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) 

        # To show in player
    if ret == True:
        cv.imshow("video", grayframe)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

