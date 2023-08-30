import cv2 as cv
import numpy as np

# loading the image
img = cv.imread("images/engineer group.jpeg")
#
# # converting image to gray scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# # blurring the image
blur = cv.GaussianBlur(grey, (3, 3), cv.BORDER_DEFAULT)
#
# getting the edges using Canny edge detection
canny = cv.Canny(blur, 125, 175)
#
# # finding contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found")

# drawing the contours on the original image
contour_img = img.copy()
cv.drawContours(contour_img, contours, -1, (0, 0, 0), 1)
#
# # showing the images
cv.imshow("Original Image", img)
cv.imshow("Canny Edge Detection", canny)
cv.imshow("Contours", contour_img)
#
cv.waitKey(0)
cv.destroyAllWindows()

width , height = img.shape[:2]
print(f"the width is {width} and the height is {height}")
cv.imshow("original", img)
#
# #resize the image
size = (600,100)
resized  = cv.resize(img, size, interpolation=cv.INTER_LINEAR)
cv.imshow("resized", resized)
#
#rotate the image
def rotate(img,angle,rotPoint=None):
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotate = rotate(img,45,rotPoint=None)
cv.imshow("rotated", rotate)
#
# #using the canny
canny = cv.Canny(img,125,175)
cv.imshow("canny", canny)
#
# #making the image grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)



