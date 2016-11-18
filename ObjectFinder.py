import cv2
import numpy as np

import ISLib as isx


## main program starts

image = cv2.imread('test/images/part.jpg', cv2.IMREAD_COLOR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ratio, resized = isx.optimalSize(gray)

ret,thresh = cv2.threshold(resized, 127, 255, cv2.THRESH_BINARY)

display = cv2.resize(image, None, fx=ratio, fy=ratio, interpolation = cv2.INTER_CUBIC)

im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(display, contours, -1, (0, 255, 0), 1)

for cont in contours:
    print(cv2.moments(cont))


cv2.imshow('Grayscaled', resized)
cv2.imshow('Thresholded', thresh)
cv2.imshow('Output', display)
cv2.waitKey(0)
cv2.destroyAllWindows()

## end of the main program
