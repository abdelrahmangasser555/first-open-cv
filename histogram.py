import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#original image
img = cv.imread('images/moratab.jpg')
cv.imshow('cinema rats', img)

#rotate the image
rotated = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)



#convert to grayscale
grey = cv.cvtColor(rotated, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)


#grey scale histogram
grey_hist = cv.calcHist([grey], [0],None , [256] , [0,256])

#creating a mask

mask = np.zeros(grey.shape[:2], np.uint8)
circle_mask = cv.circle(mask, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

#masked image
masked = cv.bitwise_and(grey, grey, mask=circle_mask)
cv.imshow('Masked Image', masked)

#masked grey scale histogram
masked_hist = cv.calcHist([masked], [0], mask, [256], [0,256])


#plot the histogram
plt.figure()
plt.title('Grey Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(grey_hist)
plt.xlim([0,256])
plt.show()

#plot the histogram
plt.figure()
plt.title('masked Grey Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(masked_hist)
plt.xlim([0,256])
plt.show()

#waitkey and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()