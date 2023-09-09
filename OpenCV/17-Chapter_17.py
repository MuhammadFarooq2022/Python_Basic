# Joining two images

import cv2 as cv
import numpy as np

img = cv.imread("Resources/Image.jpg")

# Stacking same image
# 1- Horizontal stack

hor_img = np.hstack((img, img))

# 2- Vertical stack

ver_img = np.vstack((img, img))

# cv.imshow("Horizontal", hor_img)
cv.imshow("Vertical", ver_img)
cv.waitKey(0)
cv.destroyAllWindows()

# you can only stack images with same shape (width, height, color channel) (600, 500, 3)
# we can not resize the stack image (function)
# same number of channels np function
# you have to define a function to stack multiple images of different sizes and tunes