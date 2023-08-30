#creating an image
import cv2 as cv
import numpy as np
img = cv.imread("images/engineer group.jpeg")

#usingg canny
canny = cv.Canny(img, 125, 175)

#grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blur
blur = cv.GaussianBlur(grey, (3, 3), cv.BORDER_DEFAULT)

#cropping the image

cropped = img[50:200, 200:400]

#show the images
cv.imshow("canny", canny)
cv.imshow("grey", grey)
cv.imshow("blur", blur)
cv.imshow("cropped", cropped)
cv.waitKey(0)
cv.destroyAllWindows()



