import cv2

file = cv2.FileStorage('camera_calibration.yaml', cv2.FILE_STORAGE_READ)
camera_matrix = file.getNode('camera_matrix').mat()
dist_coeffs = file.getNode('dist_coeffs').mat()
file.release()

print(f"Camera Matrix: \n{camera_matrix}")
print(f"Distortion Coefficients: \n{dist_coeffs}")
