from PIL import ImageFont, ImageDraw, Image
import os
import cv2
import numpy as np
import cv2
from keras.models import load_model
from demo import CNNModel
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
    
        if cv2.waitKey(1) == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()