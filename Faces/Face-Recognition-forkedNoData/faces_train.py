#pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'..Media Files\Faces\train'

# loading face identifier from haar cascade
haar_cascade = cv.CascadeClassifier('../../haarcascade_frontalface_default.xml')

features = []
labels = []

# training module
def create_train():
    # a person has a directory in which his/her photos are stored in files in different backgrounds/costumes/expressions/angles
    for person in people:
        # get the path for each person and the index as label
        path = os.path.join(DIR, person)
        label = people.index(person)

        # get path for each image of the person
        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
                
            # convert to gray
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # detect the face using haar cascade - FACE DETECTION (detects that the group of pixels must be a face)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # from the face extraction draw rectangles are region of interest and record as training data
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# create the training datal
create_train()
print('Training done ---------------')

# convert the data to np object
features = np.array(features, dtype='object')
labels = np.array(labels)

# use the face recognizer module - FACE RECOGNIZER (learns/identifies whose face it is)
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

# save the trained data
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
