import cv2
import numpy as np

# Đọc ảnh
image = cv2.imread('saa.png')

# Chuyển đổi sang ảnh đen trắng
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Điều chỉnh độ sáng và độ tương phản
alpha = 1.5  # Độ sáng
beta = 30   # Độ tương phản
adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Phóng to và thu nhỏ
scaled_up_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
scaled_down_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Quay ảnh
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Quay góc 45 độ
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Làm mờ và làm nổi bật
blurred_image = cv2.GaussianBlur(image, (9, 9), 0)
sharpened_image = cv2.filter2D(image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))

# Hiển thị ảnh
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Adjusted Image', adjusted_image)
cv2.imshow('Scaled Up Image', scaled_up_image)
cv2.imshow('Scaled Down Image', scaled_down_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Sharpened Image', sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
