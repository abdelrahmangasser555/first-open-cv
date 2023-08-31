import cv2 as cv
import numpy as np


img = cv.imread("images/engineer group.jpeg")
# color space conversion

# BGR to grayscale
cv.imshow("original", img)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
#bgr to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)
#converting grey scal to bgr
bgr = cv.cvtColor(grey, cv.COLOR_GRAY2BGR)
cv.imshow("bgr", bgr) 

cv.waitKey(0)
cv.destroyAllWindows()