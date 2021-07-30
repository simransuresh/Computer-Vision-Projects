# blur, gaussianblur, median, bilateral - retains edge whiele blur
# bitwise and, or, xor- or-and, not

import cv2 as cv
import matplotlib.pyplot as plt

image = cv.imread('park.jpg')
cv.imshow('park', image)

# BGR TO GRAY
bgr2gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', bgr2gray)

# BGR TO HSV
bgr2hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow('hsv', bgr2hsv)

# BGR TO LAB
bgr2lab = cv.cvtColor(image, cv.COLOR_BGR2LAB)
cv.imshow('lab', bgr2lab)

# BGR to RGB
bgr2rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
cv.imshow('RGB', bgr2rgb)

# LAB to BGR
lab2bgr = cv.cvtColor(bgr2lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab2bgr)

# GRAY TO HSV is not possible. Thus convert gray to bgr to hsv.
gray2bgr = cv.cvtColor(bgr2gray, cv.COLOR_GRAY2BGR)
bgr2hsv = cv.cvtColor(gray2bgr, cv.COLOR_BGR2HSV)
cv.imshow('GRAY TO HSV', bgr2hsv)

# names = ['original', 'bgr2gray', 'bgr2hsv', 'bgr2lab', 'bgr2rgb', 'lab2bgr', 'gray2bgr', 'bgr2hsv']
# images = image, bgr2gray, bgr2hsv, bgr2lab, bgr2rgb, lab2bgr, gray2bgr, bgr2hsv

# for index in range(8):
#     plt.subplot(3, 3, index+1)
#     plt.title(names[index])
#     plt.imshow(images[index])

# plt.show()

cv.waitKey(0)