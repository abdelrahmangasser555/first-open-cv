import cv2 as cv
import numpy as np


img = cv.imread("images/engineer group.jpeg")
cv.imshow("original", img)
blank = np.zeros(img.shape[:2], dtype="uint8")

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge tthe image

merged = cv.merge([b,g,r])
cv.imshow("merged", merged)
cv.waitKey(0)
cv.destroyAllWindows()