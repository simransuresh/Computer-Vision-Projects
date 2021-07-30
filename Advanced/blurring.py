import cv2 as cv

image = cv.imread('park.jpg')

""" Blurring - image processing technique to reduce sharpness of pixels - 'smoothing' """

# average blur with kernel window size of 3*3 - more blur as size increases
blur = cv.blur(image, (3,3))
cv.imshow('blur', blur)

# blur with gaussian weights
gaussian_blur = cv.GaussianBlur(image, (3,3), 0)
cv.imshow('gaussian blur', gaussian_blur)

# median blur technique
median_blur = cv.medianBlur(image, 3)
cv.imshow('median blur', median_blur)

# bilateral filter
bilateral_filter_blur = cv.bilateralFilter(image, 10, 35, 25)
cv.imshow('bilateral filter', bilateral_filter_blur)

cv.waitKey(0)

