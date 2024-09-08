from ultralytics import YOLO
import cv2
import numpy as np
import pyttsx3

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  # Use yolov8n.pt for the nano version or yolov8s.pt, yolov8m.pt, yolov8l.pt for larger versions

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

def give_audio_feedback(text):
    """Provides spoken feedback to the user."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Load camera calibration parameters
file = cv2.FileStorage('camera_calibration.yaml', cv2.FILE_STORAGE_READ)
camera_matrix = file.getNode('camera_matrix').mat()
dist_coeffs = file.getNode('dist_coeffs').mat()
file.release()

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Undistort frame
    undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)

    # Perform object detection
    results = model(undistorted_frame)

    # Process results
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            if confidence > 0.5:  # Confidence threshold
                if class_id == 0:  # Assuming class_id 0 is 'person'
                    give_audio_feedback("Person ahead with confidence {:.2f}".format(confidence))

    # Display the frame with detections
    annotated_frame = results.render()[0]
    cv2.imshow('Object Detection with YOLOv8', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
