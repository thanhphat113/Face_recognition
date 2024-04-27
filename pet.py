# import cv2
import numpy as np

# def save_pic(face_image,pic):
#         alpha = 1.5  # Độ sáng
#         beta = 30   # Độ tương phản
#         adjusted_image = cv2.convertScaleAbs(face_image, alpha=alpha, beta=beta)

#         # Phóng to và thu nhỏ
#         scaled_up_image = cv2.resize(face_image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
#         scaled_down_image = cv2.resize(face_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

#         # Quay ảnh
#         rows, cols = face_image.shape[:2]
#         rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Quay góc 45 độ
#         rotated_image = cv2.warpAffine(face_image, rotation_matrix, (cols, rows))

#         # Làm mờ và làm nổi bật
#         blurred_image = cv2.GaussianBlur(face_image, (9, 9), 0)
#         sharpened_image = cv2.filter2D(face_image, -1, np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]))

#         # cv2.imwrite(f'data/thunuoi/3/1_{self.count}.png',face_image)
#         cv2.imwrite(f'data/thunuoi/13/13_adjusted_{pic}.png',adjusted_image)
#         cv2.imwrite(f'data/thunuoi/13/13_up_{pic}.png.png',scaled_up_image)
#         cv2.imwrite(f'data/thunuoi/13/13_down_{pic}.png',scaled_down_image)
#         cv2.imwrite(f'data/thunuoi/13/13__rotated_{pic}.png',rotated_image)
#         cv2.imwrite(f'data/thunuoi/13/13_blurred_{pic}.png',blurred_image)
#         cv2.imwrite(f'data/thunuoi/13/13_sharpened_{pic}.png',sharpened_image)

# img = cv2.imread('data/thunuoi/13/13_5.jpeg')
# save_pic(img,5)

from keras.models import load_model
import cv2
import os

model = load_model('model/modelTN.h5')

data_dir = 'data/thunuoi'

animal_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

animals = animal_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSi

        # Lấy danh sách tên các thư mục (tương ứng với nhãn)
class_names = os.listdir(data_dir)

# Read image
image = cv2.imread('data/thunuoi/5/5_5.jpeg')
image = cv2.resize(image,(120,120))

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect animals in the image
prediction = model.predict(np.expand_dims(image, axis=0))

print(class_names[int(np.argmax(prediction))])


