# pylint: disable = no-member

import cv2
import os
import os.path
import json

X_start,  Y_start, X_stop, Y_stop, link = [], [], [], [], []

for img in range(50):
    with open("face_data_json\\{}.json".format(img + 1)) as f:
        data = json.load(f)
        shape = data["shapes"][0]
        point = shape["points"]
        X_start.append(round(point[0][0]))
        Y_start.append(round(point[0][1]))
        X_stop.append(round(point[1][0]))
        Y_stop.append(round(point[1][1]))
        link.append(data["imagePath"])

data_XY = {"X_start": X_start,
           "Y_start": Y_start,
           "X_stop": X_stop,
           "Y_stop": Y_stop,
           "link": link}

if os.path.exists("annotated_face_data_manual") == 0:
    os.makedirs("annotated_face_data_manual")

for i in range(50):
    open_img = cv2.imread("face_data\\{}".format(link[i]), 1)
    cut_img = open_img[Y_start[i]:Y_stop[i], X_start[i]:X_stop[i]]
    cv2.imwrite(
        "annotated_face_data_manual\\annotate_{}.jpg".format(i+1), cut_img)


cv2.destroyAllWindows()
