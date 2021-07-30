""" Operations like translation, rotation, resize, rescale, changing resolutions """

# importing the libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# read the image
image = cv.imread('./assets/park.jpg')
# show the original image
# cv.imshow('original', image)


""" TRANSLATION """
""" translates the image on the (x,y) coordinate -x --> Left, -y --> Up, x --> Right, y --> Down """
x, y = -100, -100
# form a matrix using numpy with given x,y coordinate
transMatrix = np.float32([[1, 0, x], [0, 1, y]])
# get the dimensions
dimensions = (image.shape[1], image.shape[0])
# form the translated image from the dimensions and matrix
translated_image = cv.warpAffine(image, transMatrix, dimensions)
# cv.imshow("translated", translated_image)


""" ROTATION """
""" rotate the given image to an angle from the rotational point +theta --> anticlockwise, -theta --> clockwise """
rotationalPoint = None
rotationalAngle = 120
# get dimensions
(height, width) = image.shape[:2]
# if point not given get the centre point
if rotationalPoint is None:
    rotationalPoint = (width//2, height//2)
# form the rotational matrix
rotationalMatrix = cv.getRotationMatrix2D(rotationalPoint, rotationalAngle, 1.0)
dimensions = (width, height)
# return the rotation on the image using the matrix and dimensions
rotated = cv.warpAffine(image, rotationalMatrix, dimensions)
rotated_again = cv.warpAffine(rotated, rotationalMatrix, dimensions)
# cv.imshow('rotate', rotated)
# cv.imshow('rotate_rotate', rotated_again)


""" RESIZING """ 
# Resizing the image to 500, 500 pixel size, The orientation will be cubic
resized = cv.resize(image, (500, 500), interpolation = cv.INTER_CUBIC)
# cv.imshow('Resized', resized)


""" RESCALING """
""" applied to Image, video and live video. changes the image scale, Try with 0.75-downscale, 1.5-upscale etc """
scale_factor = 0.5
# get width and height from shape
height = int(image.shape[0] * scale_factor)
width = int(image.shape[1] * scale_factor)
# set dimensions
dimensions = (width, height)
rescaled = cv.resize(image, dimensions, interpolation = cv.INTER_AREA)
# cv.imshow('Downscaled image', rescaled)


""" RESOLUTION """
""" changes the width and height of the capture in real time """
# get camera image and capture
capture = cv.VideoCapture(0)
(width, height) = (640, 480) 
# (width, height) = (1280, 720)
# (width, height) = (1920, 1080)
capture.set(3, width)
capture.set(4, height)

while True:
    # read the video frame by frame
    istrue, frame = capture.read()

    if istrue:
        # display it
        cv.imshow('Video', frame)

        # close once z key is pressed
        if cv.waitKey(20) & 0xFF == ord('z'):
            break

    # when waitKey is passed frame stops
    else:
        break

capture.release()
cv.destroyAllWindows()


# matplot show - images of interest
names = ['original', 'translate', 'rotate', 'rotated_again', 'resize', 'rescale']
images = image, translated_image, rotated, rotated_again, resized, rescaled
for index in range(6):
    plt.subplot(2, 3, (index + 1))
    plt.imshow(images[index])
    plt.title(names[index])

plt.show()


# wait infinitely
cv.waitKey(10)