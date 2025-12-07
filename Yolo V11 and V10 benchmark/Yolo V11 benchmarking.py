import time
import cv2
import numpy as np
import serial
import matplotlib.pyplot as plt
from twilio.rest import Client
from ultralytics import YOLO

# Initialize Arduino connection
arduino = serial.Serial('COM7', 9600, timeout=1)  
time.sleep(2)

# Twilio credentials
TWILIO_SID = "AC55769119e1598dcdc431a8be1c4ad584"
TWILIO_AUTH_TOKEN = "6b1da3a80082fb99061052ac81bdef02"
TWILIO_PHONE = "+14323028048"
RECIPIENT_PHONE = "+917339080504"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# Load YOLO model
model = YOLO('yolo11n.pt')

# Load class names
with open("coco.txt", "r", encoding="utf-8") as f:
    class_list = f.read().strip().split("\n")

# Open video files
cap1 = cv2.VideoCapture('mall1.mp4')
cap2 = cv2.VideoCapture('mall2.mp4')
cap3 = cv2.VideoCapture('mall3.mp4')

count = 0
alert_sent = False

# ⏳ Performance Data Storage
frame_times = []
yolo_times = []
fps_values = []
people_counts = []

while True:
    start_time = time.time()

    # Read frames
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()

    if not ret1 or not ret2 or not ret3:
        break  

    count += 1
    if count % 2 != 0:
        continue  

    # Resize for consistency
    frame1 = cv2.resize(frame1, (480, 360))
    frame2 = cv2.resize(frame2, (480, 360))
    frame3 = cv2.resize(frame3, (480, 360))

    # 🔹 YOLO Inference Benchmark
    yolo_start = time.time()
    results1 = model(frame1, conf=0.02, imgsz=640)
    results2 = model(frame2, conf=0.1, imgsz=640)
    results3 = model(frame3, conf=0.1, imgsz=640)
    yolo_end = time.time()

    def process_detections(frame, results):
        boxes = results[0].boxes.data.cpu().numpy()
        person_count = 0
        object_count = len(boxes)

        for box in boxes:
            x1, y1, x2, y2, _, class_id = map(int, box[:6])
            label = class_list[class_id] if class_id < len(class_list) else "unknown"

            if label == "person":
                person_count += 1
                color = (255, 0, 0)  # Blue for persons
            else:
                color = (0, 255, 0)  # Green for other objects

            # Draw bounding box & label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)
            cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return person_count, object_count

    persons1, objects1 = process_detections(frame1, results1)
    persons2, objects2 = process_detections(frame2, results2)
    persons3, objects3 = process_detections(frame3, results3)

    people_counts.append(persons1 + persons2 + persons3)

    # Display person & object count
    cv2.putText(frame1, f'Persons: {persons1} | Objects: {objects1}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame2, f'Persons: {persons2} | Objects: {objects2}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(frame3, f'Persons: {persons3} | Objects: {objects3}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # 🔹 Send Arduino Signal & SMS Alert
    if persons1 > 170 or persons2 > 60 or persons3 > 60:
        arduino.write(b'1')  # Activate buzzer & LED
        if not alert_sent:
            try:
                alert_message = "🚨 High crowd detected!"
                message = client.messages.create(
                    body=alert_message,
                    from_=TWILIO_PHONE,
                    to=RECIPIENT_PHONE
                )
                print(f"📩 SMS Sent: {message.sid}")
                alert_sent = True
            except Exception as e:
                print(f"❌ Twilio Error: {e}")
    else:
        arduino.write(b'0')  # Deactivate buzzer & LED
        alert_sent = False

    # 🔹 Compute Total Frame Processing Time
    frame_time = time.time() - start_time
    frame_times.append(frame_time)
    yolo_times.append(yolo_end - yolo_start)

    # 🔹 Calculate FPS
    fps_values.append(1 / frame_time if frame_time > 0 else 0)

    # 🔹 Show Output
    combined_frame = cv2.hconcat([frame1, frame2, frame3])
    cv2.imshow("Crowd Detection - 3 Videos", combined_frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

# 🔹 Compute Average FPS
average_fps = sum(fps_values) / len(fps_values)
print(f"\n📊 Average FPS: {average_fps:.2f}")

# 🔹 Release Resources
cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
arduino.close()

# 📈 Generate Graphs
plt.figure(figsize=(12, 6))

# 🔹 People Count Graph
plt.subplot(2, 2, 1)
plt.plot(people_counts, label="People Count", color='m')
plt.xlabel("Frame Number")
plt.ylabel("Count")
plt.title("People Count Over Time")
plt.legend()

# 🔹 Frame Processing Time Graph
plt.subplot(2, 2, 2)
plt.plot(frame_times, label="Frame Processing Time", color='b')
plt.xlabel("Frame Number")
plt.ylabel("Time (sec)")
plt.title("Frame Processing Time")
plt.legend()

# 🔹 YOLO Inference Time Graph
plt.subplot(2, 2, 3)
plt.plot(yolo_times, label="YOLO Inference Time", color='r')
plt.xlabel("Frame Number")
plt.ylabel("Time (sec)")
plt.title("YOLO Inference Time")
plt.legend()

# 🔹 FPS Graph
plt.subplot(2, 2, 4)
plt.plot(fps_values, label="FPS", color='g')
plt.xlabel("Frame Number")
plt.ylabel("Frames Per Second")
plt.title("FPS Over Time")
plt.legend()

plt.tight_layout()
plt.show()

