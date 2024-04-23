from PIL import ImageFont, ImageDraw, Image
import os
import cv2
import numpy as np
import cv2
from keras.models import load_model

<<<<<<< HEAD
from DAO.customerDAO import customerDAO
from DAO.petDAO import petDAO

def detect(object):
    data_dir = ('data/') + object
    list = os.listdir(data_dir)
    num = len(list)
    cnn = CNNModel(num_class=num)

    cnn.build_model()
    datax, datay = cnn.load_data(data_dir)
    cnn.train_model(datax, datay)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    while True:
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        result = cnn.predict_img(cnn.model,frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            index = int(np.argmax(result))

            if object == 'khachhang':
                temp = customerDAO().findByid(list[index])
                name = temp.get_tenkh()
            else:
                temp = petDAO().findById1(list[index])
                name = temp.get_tentn()

            cv2.putText(frame, str(name), (x+w+10, y+h), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    
        cv2.imshow('ahha',frame)
=======
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DAO.customerDAO import customerDAO
from DTO.customerDTO import customer

model = load_model('model/demo.h5')

data_dir = 'data/khachhang'

# Lấy danh sách tên các thư mục (tương ứng với nhãn)
class_names = os.listdir(data_dir)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
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
        
        
        if prediction.max() < 0.5:
            label = "Unknown"
        else:
            label = class_names[int(np.argmax(prediction))]
        
        kh = customerDAO()
        cus = kh.findByid(label)
        if cus is not None:
            ten = cus.get_tenkh()
        else:
            ten = 'Unknow'
        
        draw.text((x + w + 10, y + h), ten, font=font, fill=(0, 255, 0))
        frame_with_text = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
            
        cv2.rectangle(frame_with_text, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # font_scale = 1  # Thay đổi scale font
        # font_thickness = 2  # Độ dày của chữ
        # cv2.putText(frame, "Thanh Phát", (x + w + 10, y + h), font, font_scale, (0, 255, 0), font_thickness, cv2.LINE_AA)
    
    cv2.imshow('ahha',frame_with_text)
>>>>>>> 276dec78fd58833f710c7992762ceeabe1af9250
    
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()