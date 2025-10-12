# Crowd Monitoring System Using YOLOv11 with Benchmark Analysis and YOLOv10 Comparison 
## Introduction
The Crowd Monitoring System Using YOLOv11 is an advanced real-time people detection and crowd analysis framework designed to ensure safety, efficiency, and situational awareness in high density public environments. With the increasing need for automated surveillance and intelligent video analytics, this project leverages the latest YOLOv11 architecture to deliver high accuracy person detection, robust performance under occlusion, and optimized inference speed.
The system continuously monitors video feeds either from CCTV  live streams—to identify and count individuals, track movement patterns, and analyze crowd density. Its real-time capability enables authorities or organizations to detect overcrowding
To evaluate the system’s effectiveness, this project includes a comprehensive benchmark analysis comparing YOLOv11’s performance against YOLOv10 under identical conditions.
## Problem Statement
Crowding in public areas such as transportation hubs, retail outlets, event venues, and urban streets poses significant challenges related to safety, security, and operational effectiveness. When a large number of individuals gather within a confined space without proper monitoring or regulation, the risks of accidents, panic situations, and security breaches increase rapidly. Lack of real-time surveillance and automated alert mechanisms often delays response actions, leading to potential harm or disruption. Therefore, there is a critical need for an intelligent system capable of accurately detecting and analyzing crowd density in real time, ensuring timely alerts and preventive measures to maintain safety and order in high-density public environments.
## Propose System Archietecture

![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/system%20archietecturreee.jpg)
## Theoretical Description:
- This project focuses on real-time crowd density monitoring using the YOLOv11 object detection model. The system captures live video streams and detects people within each frame to calculate crowd levels accurately.
- It evaluates real-time performance parameters such as processing time, inference time, FPS, and people count. The YOLOv11 model is benchmarked against YOLOv10 to compare improvements in accuracy, speed, and detection efficiency.
- When the detected crowd exceeds a predefined threshold, the system triggers multiple alerts. An Arduino module activates a buzzer and LED for on-site notification, while a Twilio API sends SMS alerts to concerned authorities for remote monitoring.
- Additionally, all performance and detection data are stored in Excel and visualized through graphs to assist in performance analysis and system optimization.
## Tools and technolies used
| **Technology / Tool**   | **Purpose**                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| **YOLOv11 & YOLOv10**   | Deep learning-based object detection for identifying and counting people |
| **OpenCV**              | Frame capture, video stream handling, and image preprocessing            |
| **Arduino UNO**         | Controls buzzer and LED for crowd-level alerts                           |
| **Buzzer & LED**        | Hardware indicators for high crowd density alerts                        |
| **Twilio API**          | Sends SMS notifications during high crowd scenarios                      |
| **Matplotlib & Pandas** | Graph plotting, data analysis, and performance visualization             |
| **Excel**               | Stores benchmark metrics and evaluation data for analysis                |
## Working Principle
- Captures video streams, detects people & objects using YOLO.
- Calculates, processing time, inference time, FPS and people count
- If crowd exceeds a threshold:
    - Buzzer & LED activate (Arduino).
    - SMS alert sent (Twilio).
- Data is graphed & stored in Excel for analysis.
- YOLOv11 vs. YOLOv10 comparison evaluates speed & accuracy improvements.
## YOLO V11 Crowd Detection Output

![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/crowd%20detect.png)
### Observations
- The figure shows YOLOv11-based crowd detection across three different video scenes.
- Detected persons and objects are highlighted with bounding boxes — 🟦 Blue boxes for persons and 🟩 Green boxes for other objects.
- The total number of detected persons and objects is displayed at the top of each frame for real-time monitoring.
- Bounding boxes are well-aligned and consistent, confirming YOLOv11’s strong detection accuracy for both small and overlapping objects.
## Graph Analysis and Benchmark comparison
### YOLO V11 Graph
![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/11vbench.png)
### YOLO V10 Graph
![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/10vbench.png)

### Inference Time Comparison
|       Frame       |    5   |    6   |    7   |    8   |    9   |
| :---------------: | :----: | :----: | :----: | :----: | :----: |
| **YOLOv11 (sec)** | 0.2557 | 0.4282 | 0.2266 | 0.2990 | 0.3959 |
| **YOLOv10 (sec)** | 0.2451 | 0.2435 | 0.2656 | 0.2489 | 0.2398 |

### Frame Processing Time Comparison
|       Frame       |    5   |    6   |    7   |    8   |    9   |
| :---------------: | :----: | :----: | :----: | :----: | :----: |
| **YOLOv11 (sec)** | 0.2743 | 0.2628 | 0.2486 | 0.3210 | 0.4278 |
| **YOLOv10 (sec)** | 0.2656 | 0.2606 | 0.2816 | 0.2636 | 0.2558 |

Inference time and frame processing time of V10 is better when compared to v11

### People Count graph

![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/crowd%20count.png)

|    Frame    |  2  |  3  |  4  |  5  |  6  |
| :---------: | :-: | :-: | :-: | :-: | :-: |
| **YOLOv11** |  3  |  74 | 105 | 113 | 138 |
| **YOLOv10** |  3  |  49 |  50 |  57 |  55 |

- In the detection part, the YOLO V11 model is more efficient
- The project focuses on accuracy than the processing time. So, we’ve used the YOLO V11 model as our primary
## Final Result Comparison

| **Frame**                           | **YOLOv11** | **YOLOv10** | **Best Choice** |
| :---------------------------------- | :---------: | :---------: | :-------------: |
| **People Count**                    |     High    |     Low     |   **YOLOv11**   |
| **Inference Time**                  |     High    |     Low     |   **YOLOv10**   |
| **Frame Processing Time**           |     High    |     Low     |   **YOLOv10**   |
| **Overall Performance (Detection)** |    Better   |     Weak    |   **YOLOv11**   |

- This project prioritizes detection accuracy over speed.
- Hence, YOLOv11 is the better choice in this scenario, as it delivers superior detection performance even though it requires slightly more processing time.






