# pylint: disable = no-member

import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if os.path.exists("annotated_face_data_haar_cascode") == 0:
    os.makedirs("annotated_face_data_haar_cascode")

for i in range(50):
    img = cv2.imread("face_data\\{}.jpg".format(i+1))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5)
    for (X_start, Y_start, X_range, Y_range) in faces:
        cut_img = img[Y_start:Y_start+Y_range, X_start:X_start+X_range]
        cv2.imwrite(
            "annotated_face_data_haar_cascode\\annotate_{}.jpg".format(i+1), cut_img)

cv2.destroyAllWindows()
