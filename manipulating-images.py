# import cv2 as cv
# import numpy as np
# width = int(input("Enter the width of the image: "))
# height = int(input("Enter the height of the image: "))
# blank = np.zeros((width,height , 3), dtype='uint8')
# cv.rectangle(blank, (0, 0), (int(blank.shape[1]/2), int(blank.shape[0]/2)), (0, 255, 0), thickness=cv.FILLED)
# cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2), width//4, (0, 0, 255), thickness=cv.FILLED)
# cv.imshow("circle  + rectangle", blank)
# if cv.waitKey(0) == ord('q'):
#     cv.destroyAllWindows()


import cv2 as cv

video = cv.VideoCapture(0)

while True:
    is_true, frame = video.read()

    if not is_true:
        break

    top_left = (0, 0)
    bottom_right = (int(frame.shape[1] / 2), int(frame.shape[0] / 2))
    cv.rectangle(frame, top_left, bottom_right, (0, 255, 0), thickness=cv.FILLED)
    cv.putText(frame, "matgeby bosa ", (30, 40), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 255), 2)

    cv.imshow('video', frame)

    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows()
