#! /usr/bin/python

# import the necessary packages
from imutils import paths
import face_recognition
#import argparse
import pickle
import cv2
import os

class Train:
    def __init__(self):
        # our images are located in the dataset folder
        self.id_Folder = '3'
        self.dataset_Folder = '3'
        self.model_Folder = 'Model'
        self.encodingsP = "encodings.pickle"

        print("[INFO] start processing faces...")
        self.imagePaths = list(paths.list_images(f"{self.id_Folder}/{self.dataset_Folder}/"))

        # initialize the list of known encodings and known names
        self.knownEncodings = []
        self.knownNames = []
    def function(self):
        # loop over the image paths
        for (i, imagePath) in enumerate(self.imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1,
                len(self.imagePaths)))
            name = imagePath.split(os.path.sep)[-2]
            print(name)
            # load the input image and convert it from RGB (OpenCV ordering)
            # to dlib ordering (RGB)
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input image
            boxes = face_recognition.face_locations(rgb,
                model="hog")

            # compute the facial embedding for the face
            encodings = face_recognition.face_encodings(rgb, boxes)

            # loop over the encodings
            for encoding in encodings:
                # add each encoding + name to our set of known names and
                # encodings
                self.knownEncodings.append(encoding)
                self.knownNames.append(name)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")
        data = {"encodings": self.knownEncodings, "names": self.knownNames}
        f = open(f"{self.id_Folder}/{self.model_Folder}/{self.encodingsP}", "wb")
        f.write(pickle.dumps(data))
        f.close()

if __name__ == "__main__":
    train = Train()
    train.function()