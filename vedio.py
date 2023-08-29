import cv2 as cv
import numpy as np
while True:
    img = cv.imread("images/engineer group.jpeg")
    resized_img = cv.resize(img, (500, 500))
    cv.imshow("resized_img", resized_img)
    if cv.waitKey(1) == ord('q'):
        break


cv.destroyAllWindows()