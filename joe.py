import cv2 as cv
import numpy as np


blank  = np.zeros((500,500,3), dtype="uint8")

#spliting the image and coloring it

blank[0:250 , 0:250] = 0,0,255
