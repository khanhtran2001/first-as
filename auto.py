import numpy as np
import cv2
from matplotlib import pyplot as plt
import json
import os
import base64

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
