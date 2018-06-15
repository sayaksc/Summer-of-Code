import numpy as np
import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python2.7/dist-packages/cv2/data/haarcascade_frontalface_alt2.xml')
recognizer.read("trainer.yml")

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 2)
    for (x, y, w, h) in faces:
        # print x, y, w, h
        roi_color = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)
        print id_
        # img = "test.png"
        # cv2.imwrite(img, roi_color)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('video', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
