import cv2 as cv
import numpy as np

img = cv.imread("images/engineer group.jpeg")
cv.imshow("original", img)

# averaging bluriing
average = cv.blur(img, (3,3))
cv.imshow("average", average)

# gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gauss", gauss)


#median blur
median = cv.medianBlur(img, 3)
cv.imshow("median", median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)
cv.destroyAllWindows()