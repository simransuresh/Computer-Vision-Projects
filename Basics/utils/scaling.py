import cv2 as cv

# Image, video and live video
def rescaleImage(frame, scale_factor=0.5):

    # get width and height from shape
    height = int(frame.shape[0] * scale_factor)
    width = int(frame.shape[1] * scale_factor)

    # set dimensions
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)