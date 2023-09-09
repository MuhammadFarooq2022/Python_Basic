# Saving an Image or writing an Image 

import cv2 as cv

img = cv.imread("resources/Image.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
binary = cv.resize(binary,(400,500))
cv.imwrite('resources/image_gray.jpg', gray)
cv.imwrite('resources/image_B&W.jpg', binary)
# cv.waitKey(0)
# cv.destroyAllWindows()