# Basic functions or manipulation in opencv

import cv2 as cv
import numpy as np

img = cv.imread("Resources/Image.jpg")

# Resize
resized_img = cv.resize(img, (450, 250))

# Gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Blurred 
blurr_img = cv.GaussianBlur(img, (23,23), 0)

# Edge detection
edge_img = cv.Canny(img, 47,47)

# Thickness of lines
mat_kernel = np.ones((7,7), np.uint8)
dilated_img = cv.dilate(edge_img, (mat_kernel), iterations=1)

# Make thinner outline
ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)

# Cropping we will use numpy library not opencv
print("The size of our image is:", img.shape)
cropped_img = img[0:400, 250:700]

cv.imshow("Original", img)
cv.imshow("Resized", resized_img)
cv.imshow("Gray", gray_img)
cv.imshow("Blurr", blurr_img)
cv.imshow("Edge", edge_img)
cv.imshow("Dilated", dilated_img)
cv.imshow("Erosion", ero_img)
cv.imshow("Cropped", cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()