# Calibration Process

### Continuous Calibration or Pre-Calibration
Pre-Calibration: You can pre-calibrate the camera in a controlled environment, saving the intrinsic parameters (camera matrix and distortion coefficients). As long as the camera’s internal parameters (focal length, lens, etc.) remain unchanged, the same calibration parameters can be reused.

### Dynamic Calibration (if necessary)
If the camera movement introduces significant changes (like zooming or changes in focus), you might need to re-calibrate the camera dynamically during operation. However, this is less common unless you expect drastic changes in the lens system.

### Camera Usage for Object Detection in a Dynamic Environment
When the camera is moving (e.g., mounted on a visually impaired person's face), your system needs to handle varying perspectives and dynamically changing scenes. Object detection needs to adapt to the changing field of view.

Calibration Before Object Detection: In this case, you’ll calibrate the camera once or periodically, but use the calibration parameters to correct the image distortions on the fly before running object detection.

Camera Distortion: Even though the camera is moving, the distortion caused by the lens remains the same. Correcting for barrel or pincushion distortion is critical before any detection tasks to ensure that objects are accurately detected, even when the person moves their head.


### Prepare for Calibration

### Mount the Checkerboard:

Place the checkerboard on a flat surface 

![alt text](/home/sharathvn/Projects/04_Ros_dev/Real_time_camera_calibration/pattern.png)

Ensure that it is positioned such that the camera can view it from different angles.

Capture Calibration Images
Use the following script to capture images of the checkerboard pattern from various angles. The script will help collect multiple images necessary for accurate calibration.

Using 
```
python automatic_camera_calibration.py
```
4. Verify Calibration Parameters

```
 python calibration_report.py
```
Real-Time Object Detection

Follow the remaining instructions in the Real-Time Object Detection section of the README for integrating the calibrated camera with YOLOv8.

```
python real_time_object_detection.py
```

# Troubleshooting

- Camera Not Detected: Ensure the camera is properly connected and recognized by the system.
- Calibration Issues: Ensure the checkerboard is flat, clearly visible, and captured from different angles.
- Model Not Found: Confirm YOLOv8 weights are downloaded and internet access is available