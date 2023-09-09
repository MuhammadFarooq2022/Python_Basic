# Resizing an Image
# Import library
import cv2 as cv

img = cv.imread("resources/image.jpg")

img1 = cv.resize(img,(800,600))

cv.imshow("Pehli Image", img)
cv.imshow("Doosri Image", img1)
cv.waitKey(0)
cv.destroyAllWindows()