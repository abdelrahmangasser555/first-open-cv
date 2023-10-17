import cv2 as cv


vedio = cv.VideoCapture(0)


while True:
    ret , frame = vedio.read()
    if ret == True:
        cv.imshow("vedio",frame)
        if cv.waitKey(1) == ord("q"):
            break
    else:
        break

vedio.release()
cv.destroyAllWindows()