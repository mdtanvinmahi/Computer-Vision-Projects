# Detecting PPE at Construction Sites

* The goal of the project is to detect and track specific objects in a video stream. The objects of interest include personal protective equipment (PPE) items like Gloves, Hardhats, Masks, and Safety Vests, as well as other objects like vehicles and machinery.

## To run this program, we need to do it into three phases:
This is an object detection problem using a YOLO (You Only Look Once) model, a state-of-the-art deep learning model for real-time object detection. The approach follows the following phases:
**1.** **Capture video frames** – Continuously capture each frame from the video stream (in this case, the PPE video).

**2.** **Detect objects** – Use the YOLO model to identify objects in the frame (bounding boxes).

**3.** **Process the detections** – Extract information like object class, bounding box coordinates, and confidence scores.

**4.** **Display the results** – Show the objects detected on the video with bounding boxes and labels.

## Key Components and Libraries:
**1.** **YOLO (You Only Look Once):** A popular pre-trained deep learning model used for real-time object
detection. 
* It's capable of detecting multiple object classes (cars, buses, motorbikes, etc.) in
Images and videos.
* It divides the image into grid cells, where each cell predicts bounding boxes and class probabilities. YOLO is known for its speed and accuracy in real-time applications.

The code loads a pre-trained model (ppe.pt) which is fine-tuned for detecting objects like Gloves, Hardhat, Mask, Safety Vest, and various vehicles.

**2.** **OpenCV (cv2):** Used for video reading, drawing shapes, and image manipulation.
* OpenCV is a popular library used for computer vision tasks such as image processing, video reading, and writing. It provides functions for drawing shapes (bounding boxes), handling video frames, and manipulating images.

* Functions like cv2.VideoCapture() (for reading video frames) and cv2.imshow() (for displaying frames) are key to handling video input/output.

* cv2.rectangle() is used to draw bounding boxes around detected objects.

**3.** **cvzone:** cvzone is a utility library built on top of OpenCV that simplifies common tasks like overlaying text and shapes on images or video streams. 
* It provides high-level functions for handling common vision tasks such as displaying bounding boxes with labels or drawing corner rectangles.

* The code uses cvzone.cornerRect() to draw the bounding boxes with corners styled in a customized way.

* cvzone.putTextRect() is used for placing text with a rectangular background, which displays the object class name and its confidence score on the frame.

**4.** **Math library:** The math library is used for mathematical operations. In this case, it is used to calculate the confidence score of the detected objects.

## Steps:
1. Loading video and model 
2. Defining object classes
3. Framing processing loops
4. Extracting bounding boxes
5. Processing each detected objects
6. Filtering confidence
7. detection of class and filtering
8. Displaying the results