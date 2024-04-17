import cv2
import numpy as np

# Load ảnh
img = cv2.imread('data/khachhang/4/4_5.png')

# Xoay ảnh
angle = 30
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_img = cv2.warpAffine(img, M, (cols, rows))

# Phóng to và thu nhỏ
scale_percent = 200  # Phóng to 150%
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
resized_img = cv2.resize(img, (width, height))

# Lật ảnh
flipped_img = cv2.flip(img, 1)  # Lật theo chiều ngang

# Thay đổi độ sáng và độ tương phản
brightness = 80
contrast = 0.5
adjusted_img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

# Thay đổi màu sắc
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue_shift = 20
hsv_img[:, :, 0] = (hsv_img[:, :, 0] + hue_shift) % 180
color_shifted_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

# Lưu ảnh
cv2.imwrite('rotated_img.jpg', rotated_img)
cv2.imwrite('resized_img.jpg', resized_img)
cv2.imwrite('flipped_img.jpg', flipped_img)
cv2.imwrite('adjusted_img.jpg', adjusted_img)
cv2.imwrite('color_shifted_img.jpg', color_shifted_img)
