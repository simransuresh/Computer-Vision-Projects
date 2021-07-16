""" Operations like translation, rotation, resize, rescale, 
    changing resolutions, flip, crop """

# importing the libraries
import cv2 as cv
import numpy as np


# read the image
image = cv.imread('./assets/park.jpg')
# show the original image
cv.imshow('original', image)


""" TRANSLATION """
def translate(image, x, y):
    """ 
    translates the image on the (x,y) coordinate
    image: 2D image
    x: x coordinate
    y: y coordinate 
    """
    # form a matrix using numpy with given x,y
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])

    # get the dimensions
    dimensions = (image.shape[1], image.shape[0])

    # form the translated image from the dimensions and matrix
    return cv.warpAffine(image, transMatrix, dimensions)

""" -x --> Left, -y --> Up, x --> Right, y --> Down """
translated_image = translate(image, -100, -100)
cv.imshow("translated", translated_image)


""" ROTATION """
def rotate(image, angle, point=None):
    """
    rotate the given image to an angle from the rotational point
    image: given image
    angle: rotational angle
    point: rotational point 
    """
    # get dimensions
    (height, width) = image.shape[:2]

    # if point not given get the centre point
    if point is None:
        point = (width//2, height//2)

    # form the rotational matrix
    rotationalMatrix = cv.getRotationMatrix2D(point, angle, 1.0)
    dimensions = (width, height)

    # return the rotation on the image using the matrix and dimensions
    return cv.warpAffine(image, rotationalMatrix, dimensions)

""" +theta --> anticlockwise, -theta --> clockwise """
rotated = rotate(image, 120)
rotated_again = rotate(rotated, -120)
cv.imshow('rotate', rotated)
cv.imshow('rotate_rotate', rotated_again)


""" RESIZING """ 
# Resizing the image to 500, 500 pixel size, The orientation will be cubic
resized = cv.resize(image, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)


""" RESCALING """
def rescale(frame, scale_factor=0.5):
    """
    applied to Image, video and live video. changes the image scale
    frame: image or video frame
    scale_factor: amount of rescale
    """
    # get width and height from shape
    height = int(frame.shape[0] * scale_factor)
    width = int(frame.shape[1] * scale_factor)

    # set dimensions
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

cv.imshow('Downscaled image', rescale(image, scale_factor=0.75))
cv.imshow('Upscaled image', rescale(image, scale_factor=1.5))


""" RESOLUTION """
def change_resolution(width, height):
    """
    changes the width and height of the capture in real time
    width: width of the capture
    height: height of the capture
    """
    # get camera image and capture
    capture = cv.VideoCapture(0)
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

change_resolution(640, 480)
# change_resolution(1280, 720)
# change_resolution(1920, 1080)


""" FLIPPING """
""" 0 --> around the y-axis, 1 --> around x-axis, -1 --> around both axes """
flipped = cv.flip(image, 1)
cv.imshow('Flipped', flipped)


""" CROPPING """
cropped = image[10:100, 20:200]
cv.imshow('Cropped', cropped)


# wait infinitely
cv.waitKey(10)