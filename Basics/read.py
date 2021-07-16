# Import the cv library
import cv2 as cv

""" READING AN IMAGE """
img = cv.imread('./assets/cat.jpg')

# Display the image
cv.imshow('Cats', img)

# Image displays milliseconds time to close - 0 waits infinitely
cv.waitKey(0)


""" READING A VIDEO """
# Reading video from asset, 0 for real time camera capture
video = cv.VideoCapture('./assets/dog.mp4')

# Reads a video frame by frame
while True:
    # isTrue is true as long as video is displayed
    isTrue, frame = video.read()

    if isTrue:
        cv.imshow('Video', frame)

        # video plays till z key is pressed
        if cv.waitKey(20) & 0xFF == ord('z'):
            break

    # when waitKey is passed frame stops
    else:
        break

# release video capture object
video.release()
cv.destroyAllWindows()







