""" Operations include flip, crop, concatenation, split-merge """

# Importing the library
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# reading the image
image = cv.imread('./assets/park.jpg')
# cv.imshow('original', image)


""" FLIPPING """
""" 0 --> around the y-axis, 1 --> around x-axis, -1 --> around both axes """
flipped = cv.flip(image, 1)
# cv.imshow('Flipped', flipped)


""" CROPPING """
cropped = image[100:200, 20:200]
# cv.imshow('Cropped', cropped)


""" CONCATENATION """
""" concats image1, image2 in horizontal or vertical alignment """
v_concat = cv.vconcat([image, cv.flip(image, 1)])
# cv.imshow('vertical concat', v_concat)
h_concat = cv.hconcat([image, cv.flip(image, 1)])
# cv.imshow('horizon concat', h_concat)


""" SPLIT - MERGE """
""" splits the image into 3 color channels and merge them """
(chan_blue, chan_green, chan_red) = cv.split(image)

# adding a blank canvas to visualize b, g, r
blank = np.zeros(image.shape[:2], dtype='uint8')

blue = cv.merge([chan_blue, blank, blank])
green = cv.merge([blank, chan_green, blank])
red = cv.merge([blank, blank, chan_red])

cv.imshow('blue', blue)
print(chan_blue.shape)
cv.imshow('green', green)
print(chan_green.shape)
cv.imshow('red', red)
print(chan_red.shape)

merged = cv.merge([chan_blue, chan_green, chan_red])
# cv.imshow('merged image', cv.merge([chan_blue, chan_green, chan_red]))


# matplot show - images of interest
names = ['original', 'flip', 'crop', 'vconcat', 'hconcat', 'merged']
images = image, flipped, cropped, v_concat, h_concat, merged
for index in range(6):
    plt.subplot(2, 3, (index + 1))
    plt.imshow(images[index])
    plt.title(names[index])

plt.show()

# wait infinitely
cv.waitKey(0)