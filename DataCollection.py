import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Initialize webcam feed
cap = cv2.VideoCapture(0)

# Initialize HandDetector from cvzone library
detector = HandDetector(maxHands=1)

# Offset for enlarging cropped image
offset = 20

# Desired size for captured images
imgSize = 300  # Teachable Machine trains images in 300x300

# Folder to save captured images
folder = "Data/A"  # Choose a letter or label for the captured gesture
counter = 0  # Counter for the captured images

while True:
    success, img = cap.read()  # Read frame from webcam
    hands, img = detector.findHands(img)  # Detect hands in the frame

    if hands:
        hand = hands[0]  # Get details of the first detected hand
        x, y, w, h = hand['bbox']  # Get bounding box of the hand

        # Create a white canvas of desired size
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Crop the region around the hand
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape
        aspectRatio = h / w

        # Resize and place the cropped image on the white canvas
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        # Display the cropped hand image and the white canvas
        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    # Display the original webcam frame with hand annotations
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)
    if key == ord("s"):  # When 's' key is pressed, save the captured image
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(counter)
