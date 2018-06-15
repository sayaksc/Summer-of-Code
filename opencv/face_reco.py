'''Training'''

import cv2
import os
from PIL import Image
import numpy as np
import pickle

face_cascade = cv2.CascadeClassifier('/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir, "images")

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dir, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path).replace(" ", "-"))
            # print label, path
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            # y_labels.append(label)
            # x_train.append(path)
            pil_image = Image.open(path).convert("L") #Grayscale
            image_array = np.array(pil_image)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.5, minNeighbors = 2)
            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

            # print image_array
with open("labels.pickle", 'wb') as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
