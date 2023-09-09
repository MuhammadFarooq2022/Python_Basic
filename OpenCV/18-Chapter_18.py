# How to change the perspective of an image

import cv2 as cv
import numpy as np

img = cv.imread("Resources/Image.jpg")

# Defining points

point1 = np.float32([[233,196],[82,471],[522,169],[715,482]])

width = 800
height = 900
width, height = 800,900

point2 = np.float32([[0,0],[800,0],[0,900],[width, height]])

matrix = cv.getPerspectiveTransform(point1, point2)

out_img = cv.warpPerspective(img, matrix, (width, height))

# out_img = cv.resize

cv.imshow("Original", img)
cv.imshow("Transformed", out_img)
cv.imwrite("Resources/wrap_perspective.jpg", out_img)
cv.waitKey(0)
cv.destroyAllWindows()
