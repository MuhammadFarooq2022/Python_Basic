# Writing videos from cam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height =  int(cap.get(4))
out = cv.VideoWriter("Resources/Cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'p', 'G'), 30,(frame_width, frame_height), isColor=False)

while (True):
    (ret, frame) = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # To show in player
    if ret == True:
        out.write(gray_frame)
        cv.imshow("video", gray_frame)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()