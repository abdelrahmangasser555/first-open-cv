import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")
#here is an a rectangle on the image
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (0,255,0), -1)
cv.imshow(r"rectangle on the image", rectangle)

#here is a circle on the image
circle = cv.circle(blank.copy(), (450,450), 150, (0,255,0), -1)
cv.imshow("circle", circle)


#using bitwise and is the instersection between the two images
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise_and", bitwise_and)

#using bitwise or tyo find all the reagions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)

#using bitwise xor to find the non intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("bitwise_xor", bitwise_xor)

#bitwise not inverts the binary color
bitwise_not = cv.bitwise_not(rectangle,circle)
cv.imshow("bitwise_not", bitwise_not)

#key waity and destroy all windows
cv.waitKey(0)
cv.destroyAllWindows()

