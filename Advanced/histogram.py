import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

""" Histogram visualizes the pixel intensity of the image or number of pixels at each different intensity value """

img = cv.imread('park.jpg')
cv.imshow('park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

# Gray histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ['blue', 'green', 'red']
for index, color in enumerate(colors):
    color_hist = cv.calcHist([img], [index], mask, [256], [0,256])
    plt.plot(color_hist, color=color)
    plt.xlim([0,256])
    plt.ylim([0, 1500])
plt.show()

cv.waitKey(0)