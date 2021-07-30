""" Operations include: blank, canvas, rectangle, circle, line, text """

# Importing the computer vision library
import cv2 as cv
import numpy as np


""" BLANK CANVAS """
# Drawing a blank canvas using numpy zeros
blank = np.zeros((500, 500, 3), dtype='uint8')

# Splicing a part of canvas and coloring it
blank[200:300, 300:400] = 255, 0, 255


""" RECTANGLE """
# start point, dimensions, color, thickness of rectangle - negative one fills the image
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=5)


""" CIRCLE """
# centre point, radius, color, thickness of circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=5)


""" LINE """
# start point, end point, color, thickness of line
cv.line(blank, (100, 200), (200, 300), (0, 255, 255), thickness=3)


""" TEXT """
# text, start point, font, font size, color, font thickness of text
cv.putText(blank, 'Hello, my name is Simran!!!', (0,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)


# display the canvas
cv.imshow('blank', blank)


cv.waitKey(0)