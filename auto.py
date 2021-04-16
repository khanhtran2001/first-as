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
