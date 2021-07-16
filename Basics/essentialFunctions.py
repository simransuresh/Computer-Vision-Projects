""" Operations include: Gray, Gaussian Blur, Canny, Dilation, Erosion, 
    Threshold, Inverse threshold, Adaptive threshold, contours """

# Importing the computer vision library
import cv2 as cv


# reading the image
img = cv.imread('./assets/park.jpg')
cv.imshow('original', img)


""" GRAY """
# converting the image to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


""" BLUR """
# adding noise or blurring the image - less than 5
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)


""" EDGE CASCASE - CANNY """
# finding the edge cascade using canny algo
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)


""" DILATION """
# increase number of pixels around the boundary
dilated = cv.dilate(canny, (7, 7), iterations = 3)
cv.imshow('Dilated', dilated)


""" EROSION """
# reduce number of pixels around the boundary
eroded = cv.erode(dilated, (7, 7), iterations = 3)
cv.imshow('eroded', eroded)


""" THRESHOLDING """
# threshold is the bar above which pixels convert to black below which it turns white
thresholded, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)


""" INVERSE THRESHOLD """
# inverse of threshold is applied where pixels above thres turn white and below it turns black
inv_thresholded, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded Inverse', thresh_inv)


""" ADAPTIVE THRESHOLD """
# adaptive threshold technique applied
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11,9)
cv.imshow('adaptive Thresholding', adaptive_thresh)


""" CONTOURS """
# finding the contours of the image. It needs to undergo threshold or canny before contour finding
# RETR_TREE - takes into account all the parent and child contours and its relationship
contours, hierarchy = cv.findContours(adaptive_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

# draw the contours found
cv.drawContours(adaptive_thresh, contours, -1, (0,0,255), 1)


# showing the final image of contour
cv.imshow('contours', adaptive_thresh)

# display the image infinitely until a key is pressed 
cv.waitKey(0)