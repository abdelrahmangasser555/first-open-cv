import cv2 as cv
vedio  = cv.VideoCapture(0)

while True:
    ret, frame = vedio.read()
    cv.imshow('vedio', frame)
    if cv.waitKey(1) == ord('q'):
        break
vedio.release()
cv.destroyAllWindows()
