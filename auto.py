import numpy as np
import cv2
from matplotlib import pyplot as plt
import json
import os
import base64

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image_dir = "face_data"

if os.path.exists("auto_anotation") == 0:
    os.makedirs("auto_anotation")
    
if os.path.exists("auto_anotation_json") == 0:
    os.makedirs("auto_anotation_json")

for each_img in os.listdir(image_dir):
    per_dir = os.path.join(image_dir, each_img)
    img = cv2.imread(image_dir+"/"+each_img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    origin_H, origin_W, _ = img.shape
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (X_start, Y_start, X_range, Y_range) in faces:
        new_img = img[Y_start:Y_start+Y_range, X_start:X_start+X_range]
        cv2.imwrite("auto_anotation/"+ each_img, new_img)

        with open(image_dir+"/"+each_img, "rb") as image_file:
                encode_image = base64.b64encode(image_file.read())
