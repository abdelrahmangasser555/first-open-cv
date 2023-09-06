import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#original image
img = cv.imread('images/moratab.jpg')

#rotating the image
rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow("rotated" , rotated)

#convert to grayscale
grey = cv.cvtColor(rotated, cv.COLOR_BGR2GRAY)

#simple thresholding
threshhold, thresh = cv.threshold(grey, 200, 255, cv.THRESH_BINARY)
print(threshhold)
cv.imshow('simple thresholded', thresh)

#inverse thresholding
threshhold, thresh_inv = cv.threshold(grey, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('inverse thresholded', thresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(grey , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY_INV , 13 , 3)
cv.imshow('adaptive thresholded', adaptive_thresh)


#waitkey and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()

