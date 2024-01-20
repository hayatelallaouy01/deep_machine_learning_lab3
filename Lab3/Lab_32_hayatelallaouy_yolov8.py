# Lab32 : YOLOV8
# Réalisé par : Hayat el allaouy /Emsi 2023-2024

from ultralytics import YOLO
import cv2 # computer vision library

model = YOLO('yolov8n.pt')  #savefrom.net
video_path = './test1.mp4'
cap = cv2.VideoCapture(video_path)
ret = True
while ret:
    ret, frame = cap.read()
    if ret:
        results = model.track(frame, persist=True)
        frame_ = results[0].plot()
        cv2.imshow('frame', frame_)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
