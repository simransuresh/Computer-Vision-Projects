import cv2 as cv
import numpy as np

image = cv.imread('park.jpg')

# apply gradient only on gray image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# gradient or slope detection is the key word used for edge detection
# Laplacian: Laplace of Gaussian, Mexican hat
# IDENTIFIES ZERO CROSSING
# Gaussian --> Derivative of Gaussian --> Laplacian of Gaussian
laplacian = cv.Laplacian(gray, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv.imshow('laplacian filter', laplacian)


# Sobel: derivative filter - weighted average and scaling together is sobel
# other d-filters: scharr, prewitt, roberts. d-filters reduce noise, IDENTIFY PEAKS
# smoothing is important before running filter
# image with noise/edges --> Gaussian kernel --> smoothing --> Derivative output
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel', combined_sobel)


# multi stage edge detection
# noise reducation --> grad intensity --> non max suppression --> hysteresis thresholding
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)