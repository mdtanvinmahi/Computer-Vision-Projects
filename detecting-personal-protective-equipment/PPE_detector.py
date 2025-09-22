from ultralytics import YOLO
import cv2
import cvzone
import math
# The below code is for training model.
# After training, from the 8th line to the 18th line should be commented out for testing the model.
# # Load model
# model = YOLO("../Yolo-Weights/yolo11n.pt")
# #
# # # Train model
# model.train(
#     data = "../Project -3_Personal Protective Equipment Tracking/ConstructionSiteSafety/data.yaml",
#     epochs = 70,
#     imgsz = 640,
#     task = "detect"
# )


cap = cv2.VideoCapture("../Videos/ppe-5-1.mp4")

model = YOLO("ppe.pt")

classNames = ['Excavator', 'Gloves', 'Hardhat', 'Ladder', 'Mask', 'NO-Hardhat', 'NO-Mask',
              'NO-Safety Vest', 'Person', 'SUV', 'Safety Cone', 'Safety Vest', 'bus',
              'dump truck', 'fire hydrant', 'machinery', 'mini-van', 'sedan', 'semi',
              'trailer', 'truck and trailer', 'truck', 'van', 'vehicle', 'wheel loader']

myColor = (0, 0, 255)

while True:
    success, img = cap.read()
    results = model(img, stream = True)
    # when we write stream = True, it creates generators to make the program more efficient.

    # If we want to add individual bounding boxes:
    # (
    for r in results:
        boxes = r.boxes
        # now, we have to loop through the boxes
        for box in boxes:
            # We have to find the x,y of each of the bounding boxes.
            # We can either use xyxy, or xywh. w = width and h = height
            x1, y1, x2, y2 = box.xyxy[0]
            # If we don't use [0] or the first element, we will see error because the coordinates would be packed inside, and won't show any result.
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # If we don't use the int() function, we will get the tensor values of x, y in floating points which will lead us to error.
            # To fix this, we used the int() function for the values.
            print(x1,y1, x2, y2)
            # To show the rectangles: cv2.rectangle(img, coordinates of the boxes, color code, thickness)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255, 0, 255),3)
    #       If we want to provide a customized rectangle, we can do it using the cvzone package.
    #       cvzone.cornerRect(img, bounding box)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

            # Confidence
            conf = math.ceil((box.conf[0]*100))/100
            print(conf)

            # Class name
            cls = int(box.cls[0])

            currentClass = classNames[cls]

            if conf > 0.5:
                if currentClass == 'Gloves' or currentClass == 'Hardhat' or currentClass == 'Mask' or currentClass == 'Safety Vest':
                    myColor = (0, 255, 0)

                elif currentClass == 'NO-Hardhat' or currentClass == 'NO-Mask' or currentClass == 'NO-Safety Vest':
                    myColor = (0, 0, 255)

                else:
                    myColor = (255, 0, 0)

                cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                               (max(0, x1), max(35, y1 - 5)), scale = 1.5, thickness = 2,
                               colorB = myColor, colorT = (0, 0, 0), colorR = myColor,
                               offset = 10)

                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)