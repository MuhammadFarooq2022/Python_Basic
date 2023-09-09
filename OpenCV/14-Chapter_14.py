# How to draw lines and shapes in python

import cv2 as cv
import numpy as np

# Draw a canvas 0 is for Black
img = np.zeros((600,600)) # Black
img1 = np.ones((600,600)) # White

# Print size
print("The size of our canvas is:", img.shape)

# Adding colors to the canvas
colored_img = np.zeros((600,600, 3), np.uint8) # color channel addition
colored_img[:] = 255,0,255 # color complete image
colored_img[150:230, 100:500] = 255,168,10 # part of image to be colored

# Adding line
cv.line(colored_img, (0,0), (colored_img.shape[0], colored_img.shape[1]), (255,0,0), 3) # crossed line
cv.line(colored_img, (100,100), (300,300), (255,255,50), 3) # part line

# Adding rectangles
cv.rectangle(colored_img, (50, 100), (300, 400), (255,255,255), 3) # draw
cv.rectangle(colored_img, (50, 100), (300, 400), (255,255,255), cv.FILLED) # fill

# Adding circle
cv.circle(colored_img, (400,300), 50, (255, 100,0), 5)
cv.circle(colored_img, (400,300), 50, (255, 100,0), cv.FILLED)

# Adding text
cv.putText(colored_img, "Python ka Chilla on Codanics Youtube Channel", (100,500), cv.FONT_HERSHEY_COMPLEX, .5, (255,255,0), 1)

#cv.imshow("Black", img)
#cv.imshow("White", img1)
cv.imshow("Colored", colored_img)
cv.waitKey(0)
cv.destroyAllWindows()