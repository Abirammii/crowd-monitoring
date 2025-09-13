import cv2
import numpy as np
from ultralytics import YOLO

#
model = YOLO('yolo11n.pt')  # Use 'yolov8l.pt' for better accuracy

# Define the detection area
area1 = np.array([(0,1), (0,499), (1016,499), (1019,2)], np.int32)

# Load COCO class names
with open("coco.txt", "r") as f:
    class_list = f.read().split("\n")

# Initialize Video Capture
cap = cv2.VideoCapture('mall2.mp4')

# Frame counter
count = 0

while cap.isOpened():    
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 2 != 0:  # Skip alternate frames for efficiency
        continue

    frame = cv2.resize(frame, (1020, 500))

    # Object detection with lower confidence and increased image size
    results = model(frame, conf=0.06, imgsz=720)  # Lower conf & increase size for small detections
    boxes = results[0].boxes.data.cpu().numpy()  # Convert to NumPy array
    
    person_count = 0
    object_count = 0

    # Draw bounding boxes & count objects
    for box in boxes:
        x1, y1, x2, y2, _, class_id = map(int, box[:6])
        label = class_list[class_id]
        
        if label == 'person':
            person_count += 1
            color = (0, 255, 0)  # Green for persons
        else:
            object_count += 1
            color = (0, 0, 255)  # Red for other objects

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Draw detection area
    cv2.polylines(frame, [area1], isClosed=True, color=(255, 0, 0), thickness=2)
    
    # Display counts on screen
    cv2.putText(frame, f'Persons: {person_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(frame, f'Other Objects: {object_count}', (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Small Person Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

cap.release()
cv2.destroyAllWindows()
