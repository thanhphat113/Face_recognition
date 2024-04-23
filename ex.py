from PIL import ImageFont, ImageDraw, Image
import os
import cv2
import numpy as np
import cv2
from keras.models import load_model
from trainModel import CNNModel
from DAO.customerDAO import customerDAO
from DTO.customerDTO import customer

model = load_model('model/modelKH.h5')

data_dir = 'data/khachhang'

# Lấy danh sách tên các thư mục (tương ứng với nhãn)
class_names = os.listdir(data_dir)

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if ret:
        for (x, y, w, h) in faces:
            face_image = frame[y:y+h, x:x+w]
            face_image_rgb = cv2.cvtColor(face_image,cv2.COLOR_BGR2RGB)
            face_image_rgb = cv2.resize(face_image_rgb,(120,120))
        
        
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        

    # Tạo một đối tượng ImageDraw để vẽ trên hình ảnh
            draw = ImageDraw.Draw(frame_pil)

    # Khai báo font và kích thước của nó
            font = ImageFont.truetype("Arial.ttf", 20)
            
            
            prediction = model.predict(np.expand_dims(face_image_rgb, axis=0))
            
            
            if prediction.max() < 0.9:
                label = "unknown"
                color = (255,0,0)
                color_rec = (0, 0, 255)
                
            else:
                id = class_names[int(np.argmax(prediction))]
                kh = customerDAO()
                cus = kh.findByid(id)
                label = cus.get_tenkh()
                color = (0,255,0)
                color_rec = (0,255,0)
            
            
            draw.text((x + w + 10, y + h), label, font=font, fill=color)
            frame_with_text = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
            
            cv2.rectangle(frame_with_text, (x, y), (x+w, y+h), color_rec, 2)
            
                
            
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # font_scale = 1  # Thay đổi scale font
            # font_thickness = 2  # Độ dày của chữ
            # cv2.putText(frame, "Thanh Phát", (x + w + 10, y + h), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)
        
            cv2.imshow('ahha',frame_with_text)
        
        
    else: print("Không mở được camera!")
    
    if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()