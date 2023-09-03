import cv2 as cv
import numpy as np

#masking the files
#original image
img = cv.imread('images/engineer group.jpeg')
cv.imshow('enginnering group ', img)

#blank image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

#mask
start = (blank.shape[1]//2, blank.shape[0]//2)
# mask = cv.rectangle(blank, (start[0]-100, start[1]-100), (start[0]+100, start[1]+100), 255, -1 )
mask_text = cv.putText(blank, 'Mask', (start[0]-200, start[1]+20), cv.FONT_HERSHEY_TRIPLEX, 5.0, 255, 20)
cv.imshow('Mask', mask_text)

#masked image
masked = cv.bitwise_and(img, img, mask=mask_text)
cv.imshow('Masked Image', masked)


#key waity and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()