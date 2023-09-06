import cv2 as cv
import numpy as np

#original image
img = cv.imread('images/cinema rats.jpg')
cv.imshow('cinema rats', img)

#resizing the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('resized', resized)


#laplacian
lap = cv.Laplacian(resized, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel
sobelx = cv.Sobel(resized , cv.CV_64F , 1,0)
sobely = cv.Sobel(resized , cv.CV_64F , 0,1)
combine = cv.bitwise_or(sobelx , sobely)


#displaying the image
cv.imshow("sobel x axis " , sobelx)
cv.inshow("sobel y axis " , sobely)


#canny edge detection
canny = cv.Canny(resized, 150, 175)
cv.imshow('canny', canny)



#waitkey and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()