#모델을 적용시켜서 카메라를 켜봅니다.
import torch
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='학습시킨 pt파일 경로')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    ret, frame = cap.read()

    results = model(frame)
    detections = results.pandas().xyxy[0]
    detections = detections[detections['confidence'] >= 0.7]
    print(detections)
    cv2.imshow('YOLO',np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
