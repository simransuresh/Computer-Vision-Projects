import cv2 as cv

# get camera image and capture
capture = cv.VideoCapture(0)

# changes the width and height of the capture
def change_resolution(width, height):
    capture.set(3, width)
    capture.set(4, height)

change_resolution(640, 480)
# change_resolution(1280, 720)
# change_resolution(1920, 1080)

while True:
    # read the video frame by frame
    istrue, frame = capture.read()

    if istrue:
        # display it
        cv.imshow('Video', frame)

        # close once z key is pressed
        if cv.waitKey(20) & 0xFF==ord('z'):
            break

    # when waitKey is passed frame stops
    else:
        break

capture.release()
cv.destroyAllWindows()








