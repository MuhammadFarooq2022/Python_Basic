# Image into Black and White 

import cv2 as cv

img = cv.imread("resources/Image.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

cv.imshow('original', img)
cv.imshow('gray', gray)
cv.imshow('Black and White', binary)
cv.waitKey(0)
cv.destroyAllWindows()
