from ultralytics import YOLO
model = YOLO("yolo11n.pt")
results = model("D:\project_finalsem\yolov11\mall.mp4", save=True, show=True) 