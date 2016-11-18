import cv2 as cv
import numpy as np
from PIL.Image import *
import matplotlib.pyplot as plt


image = cv.imread('test/images/lenna.png', 1)


histo = cv.calcHist([image],[0],None,[256],[0,256])


plt.subplot(121),plt.imshow(image),plt.title('Input')
# plt.subplot(122),plt.imshow(histo),plt.title('Histogram')
plt.hist(image.ravel(), 256, [0, 256]);
plt.show()

plt.show()

