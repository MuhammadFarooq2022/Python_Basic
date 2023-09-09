# Saving HD recording of cam streaming

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

# Resolution HD (1280x720)
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
#sd_resolution()
hd_resolution()
#fhd_resolution()

# Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height =  int(cap.get(4))
out = cv.VideoWriter("Resources/Cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'p', 'G'), 30,(frame_width, frame_height))

while (True):
    (ret, frame) = cap.read()
    # To show in player
    if ret == True:
        out.write(frame)
        cv.imshow("video", frame)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()