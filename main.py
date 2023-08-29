import cv2 as cv
import numpy as np

vedio = cv.VideoCapture(0)

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shaope[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
while True:
    isTrue , frame = vedio.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('vedio_resized', frame_resized)
    if cv.waitKey(1) == ord('q'):
        break
vedio.release()
cv.destroyAllWindows()

