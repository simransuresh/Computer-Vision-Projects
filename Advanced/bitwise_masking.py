import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

cv.imshow('circle', circle)
cv.imshow('rectangle', rectangle)

# bitwise operations
bitwise_and = cv.bitwise_and(circle, rectangle)
cv.imshow('and', bitwise_and)

bitwise_or = cv.bitwise_or(circle, rectangle)
cv.imshow('or', bitwise_or)

bitwise_xor = cv.bitwise_xor(circle, rectangle)
cv.imshow('xor', bitwise_xor)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('not', bitwise_not)


# masking operations
image = cv.imread('park.jpg')
cv.imshow('park', image)

blank = np.zeros(image.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (image.shape[1]//2 + 45, image.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('mask', weird_shape)

masked=cv.bitwise_and(image, image, mask=weird_shape)
cv.imshow('masked image', masked)

cv.waitKey(0)