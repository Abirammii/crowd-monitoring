import cv2
import numpy as np
import serial
import time
import yt_dlp
from twilio.rest import Client
from ultralytics import YOLO

# 🔹 Setup Arduino Serial Communication (Check COM port)
arduino = serial.Serial('COM7', 9600, timeout=1)  
time.sleep(2)

# 🔹 Twilio API Credentials
TWILIO_SID = "AC7325c0128c43107d69561f18fa88d5bb"
TWILIO_AUTH_TOKEN = "aaf7c871ec5d905d7c971b94ca30b26b"
TWILIO_PHONE = "+16292804217"  # Twilio number
RECIPIENT_PHONE = "+917339080504"  # Your phone number

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

# 🔹 Load YOLO11 model
model = YOLO('yolo11n.pt')

# 🔹 YouTube Live URL (Replace with your stream)
YOUTUBE_URL = "https://www.youtube.com/watch?v=cH7VBI4QQzA"

# 🔹 Get the direct video stream link
ydl_opts = {'format': 'best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(YOUTUBE_URL, download=False)
    stream_url = info_dict["url"]

# 🔹 Open YouTube Live stream
cap = cv2.VideoCapture(stream_url)

alert_sent = False  # Flag to prevent multiple alerts

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to read stream. Retrying...")
        time.sleep(2)
        continue

    frame = cv2.resize(frame, (1020, 500))

    # 🔹 Object detection
    results = model(frame, conf=0.1, imgsz=720)
    boxes = results[0].boxes.data.cpu().numpy()  

    person_count = 0

    # 🔹 Draw bounding boxes
    for box in boxes:
        x1, y1, x2, y2, conf, class_id = map(int, box[:6])
        
        if class_id == 0:  # Person detection
            person_count += 1
            color = (0, 255, 0)  # Green for person
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"Person {conf:.2f}", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # 🔹 Display count
    cv2.putText(frame, f'Persons: {person_count}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # 🔹 Control Arduino based on crowd size
    if person_count > 500:
        arduino.write(b'1')  # LED ON, Buzzer ON
        if not alert_sent:
            message = client.messages.create(
                body=f"🚨 Alert! High crowd detected: {person_count} people!",
                from_=TWILIO_PHONE,
                to=RECIPIENT_PHONE
            )
            print(f"📩 SMS Sent: {message.sid}")
            alert_sent = True
    else:
        arduino.write(b'0')  # LED OFF, Buzzer OFF
        alert_sent = False

    cv2.imshow("YouTube Live Crowd Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit on ESC key
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
