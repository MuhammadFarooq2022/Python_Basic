# grayscal convertion
# Import library
import cv2 as cv
import numpy as np

img = cv.imread("resources/image.jpg")

img = cv.resize(img,(800,600))

# convertion
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# display code
cv.imshow("Pehli Image", img)
cv.imshow("Gray Image", gray_img)

# delay code
cv.waitKey(0)
cv.destroyAllWindows()