# ASL Gesture Detection Project

## Introduction
This project focuses on creating a real-time American Sign Language (ASL) gesture detection system using computer vision and machine learning techniques. The system captures hand gestures through a webcam feed, processes the images, and uses a trained machine learning model to predict the corresponding ASL letter or symbol. This repository contains the code for three main steps of the project: Data Collection, Training, and Testing.

## Project Overview

### 1. Data Collection
The **Data Collection** step involves capturing hand gesture images and preparing them for training. OpenCV and the cvzone library are utilized to detect and crop the hand region from the webcam feed. The cropped images are then resized to a consistent dimension for compatibility with the machine learning model. These images are saved in a designated folder for later use in training.

### 2. Training
In the **Training** step, the dataset of hand gesture images is used to train a machine learning model. Teachable Machine, a user-friendly web tool, is employed to train the model. The tool allows for easy labeling and training of gestures, generating a trained model and corresponding code for prediction. The model is then integrated into the project to make real-time predictions based on the gestures captured by the webcam.

### 3. Testing
The **Testing** step uses the trained model to classify ASL gestures in real time. The OpenCV-based HandDetector is employed to locate the hand in the webcam feed. The captured hand region is preprocessed to match the training data's dimensions, and the trained model is used to predict the corresponding ASL letter or symbol. The predicted label is then displayed on the screen along with a visual indication of the hand's region.

## Usage
1. **Data Collection**: Run the `DataCollection.py` script to capture and save hand gesture images in the specified folders.

2. **Training**: Use Teachable Machine to upload the collected images and train a machine learning model. Download the trained model and labels file (`keras_model.h5` and `labels.txt`).

3. **Testing**: Run the `Test.py` script to perform real-time ASL gesture detection using the trained model.

## Note
- The trained model (`keras_model.h5`) is included in this repository.
- The dataset used for training is not included in the repository due to size considerations.


## References
- [CVzone Website](https://www.computervision.zone/)
- [Teachable Machine](https://teachablemachine.withgoogle.com/)
- [Murtaza's Workshop YouTube Channel](https://www.youtube.com/@murtazasworkshop)

Feel free to customize and improve upon this project according to your needs and learning objectives. Happy coding!