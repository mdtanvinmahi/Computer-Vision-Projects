# Tracking and Counting Vehicles on Road

* The goal of this project is to count cars in a video, ideally tracking each individual vehicle as it moves across a predefined region.
* This problem is based on object detection and tracking techniques.

## To run this program, we need to do it into three phases:
**1.** **Object Detection:** First, the system detects all objects (vehicles and other items) in each
frame of the video.

**2.** **Tracking:** It then tracks these detected objects across subsequent frames. Each object gets
a unique ID.

**3.** **Counting:** Whenever a tracked object crosses a specific line on the screen (defined
by limits), it is counted as passing the boundary (i.e., entering or leaving the scene).

## Key Components and Libraries:
**1.** **YOLO (You Only Look Once):** A popular pre-trained model used for real-time object
detection. It's capable of detecting multiple object classes (cars, buses, motorbikes, etc.) in
Images and videos.

**2.** **SORT (Simple Online and Realtime Tracking):** A tracking algorithm that assigns unique
IDs to detected objects and updates their positions across frames.

**3.** **OpenCV (cv2):** Used for video reading, drawing shapes, and image manipulation.

**4.** **cvzone:** A utility library to simplify overlaying text and shapes on images.

## Steps:
1. Initialize and load video
2. Load the YOLO model
3. Set up object classes
4. Mask image for Region of Interest (ROI)
5. Initialize vehicle tracking (SORT)
6. Frame processing loop
7. Vehicle detection with YOLO
8. Collect and filter detected Vehicles
9. Tracking the vehicles
10. Drawing the detection and tracking results
11. Counting the vehicles
12. Displaying results