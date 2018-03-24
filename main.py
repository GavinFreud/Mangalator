import cv2
import numpy as np


image = cv2.imread('img_1.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cv2.imwrite("grey.png", grayscale)