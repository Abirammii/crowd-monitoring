# Crowd Monitoring System Using YOLOv11 with Benchmark Analysis and YOLOv10 Comparison 
## Introduction
The Crowd Monitoring System Using YOLOv11 is an advanced real-time people detection and crowd analysis framework designed to ensure safety, efficiency, and situational awareness in high density public environments. With the increasing need for automated surveillance and intelligent video analytics, this project leverages the latest YOLOv11 architecture to deliver high accuracy person detection, robust performance under occlusion, and optimized inference speed.
The system continuously monitors video feeds either from CCTV  live streams—to identify and count individuals, track movement patterns, and analyze crowd density. Its real-time capability enables authorities or organizations to detect overcrowding
To evaluate the system’s effectiveness, this project includes a comprehensive benchmark analysis comparing YOLOv11’s performance against YOLOv10 under identical conditions.
## Problem Statement
Crowding in public areas like transportation centers, retail outlets, event locations, and urban streets poses major issues concerning safety, security, and operational effectivess. when many induviduals come together in a limited space without sufficient oversight and regulation, the dangers can increase quikly.
## Propose System Archietecture

![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/system%20archietecturreee.jpg)
## Theoretical Description:
This project monitors crowd density using YOLOv11, analyzing real-time performance and benchmarking it against YOLOv10. It integrates Arduino-controlled buzzer & LED alerts and Twilio SMS notifications for high crowd levels.
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
## Crowd Detection Output

![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/crowd%20detect.png)
## Graph Analysis and Benchmark comparison
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

### YOLO V11 Graph
![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/11vbench.png)
### YOLO V10 Graph
![Dashboard preview](https://github.com/Abirammii/crowd-monitoring/blob/main/10vbench.png)







