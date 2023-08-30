import cv2 as cv
import numpy as np
image = cv.imread("images/engineer group.jpeg")
resized_img = cv.resize(image, (500, 500), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(3000)
cv.destroyAllWindows()

