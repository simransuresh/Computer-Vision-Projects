import cv2 as cv
import utils.scaling as scale

# Reading video
video = cv.VideoCapture('./assets/dog.mp4')

# Reads a video frame by frame
while True:
    # isTrue is true as long as video is displayed
    isTrue, frame = video.read()

    if isTrue:
        cv.imshow('Video', frame)
        cv.imshow('Downscaled video', scale.rescaleImage(frame, scale_factor=0.75))
        cv.imshow('Upscaled video', scale.rescaleImage(frame, scale_factor=1.5))

        if cv.waitKey(20) & 0xFF==ord('z'):
            break

    # when waitKey is passed frame stops
    else:
        break

# release video capture object
video.release()
cv.destroyAllWindows()