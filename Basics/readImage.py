import cv2 as cv
import utils.scaling as scale

# Reading an image
img = cv.imread('./assets/cat.jpg')

# Display the image
cv.imshow('Cats', img)

# Image resizing or rescaling
cv.imshow('Resized image', scale.rescaleImage(img))

# Image displays milliseconds time to close - 0 waits infinitely
cv.waitKey(0)









