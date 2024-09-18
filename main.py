# OBJECT DETECTION
# ================
# Code Written by Jishnu Setia
# Contact: jishnusetia8@gmail.com
# ================
# This code is used to detect objects in an image using YOLOv5
# It uses the OpenCV library for image processing and the PyTorch library

import torch
import cv2
import numpy as np

# Load the pre-trained YOLOv5 model (COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Initialize camera feed (0 is the default camera, use other integers for external cameras)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform inference on the frame
    results = model(frame)

    # Extract predictions
    detections = results.pandas().xyxy[0]  # Bounding boxes, confidence, class

    # Draw bounding boxes and labels on the frame
    for _, row in detections.iterrows():
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = f"{row['name']} {row['confidence']:.2f}"
        
        # Draw rectangle and label on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Display the resulting frame with bounding boxes
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
