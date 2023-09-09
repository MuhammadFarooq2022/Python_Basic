# Reading and displaying an image
# Import library
import numpy as np
import cv2 as cv


img = cv.imread("resources/image.jpg")

cv.imshow("Pehli Image", img)
cv.waitKey(0)

