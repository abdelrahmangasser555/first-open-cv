import cv2 as cv
import numpy as np

# color space conversion
img = cv.imread("images/engineer group.jpeg")
cv.imshow("original", img)
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)
cv.waitKey(3000)
cv.destroyAllWindows()