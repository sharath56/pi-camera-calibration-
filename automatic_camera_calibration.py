import cv2
import numpy as np

# Define checkerboard dimensions
CHECKERBOARD = (9, 6)
objpoints = []
imgpoints = []

# Create a VideoCapture object
cap = cv2.VideoCapture(0)
print("Move the camera around a checkerboard pattern")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
        objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
        objpoints.append(objp)
        imgpoints.append(corners)

        # Display the corners
        cv2.drawChessboardCorners(frame, CHECKERBOARD, corners, ret)

    cv2.imshow('Calibration', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Perform calibration
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Save calibration parameters
file = cv2.FileStorage('camera_calibration.yaml', cv2.FILE_STORAGE_WRITE)
file.write('camera_matrix', camera_matrix)
file.write('dist_coeffs', dist_coeffs)
file.release()

print("Calibration complete and saved!")
