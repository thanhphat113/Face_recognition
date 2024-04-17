
import numpy as np
import cv2
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os


class CNNModel:
    def __init__(self, count = 1, input_shape=(120, 120, 3)):
        self.input_shape = input_shape
        self.count = count
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Conv2D(16, (3,3), activation='relu', input_shape=self.input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Conv2D(32, (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Conv2D(64, (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dense(self.count, activation='softmax'))
        return model

    def compile_model(self):
        self.model.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
        
    def save_model(self, model, path):
        model.save(path)
    
    def predict_img(self, model:keras.Model, img):
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (120, 120))
        img = img.reshape(-1, 120, 120, 3)
        img = img.astype('float32') / 255.0
        
        return model.predict(img)
        
    def load_data(self,folder_path, input_shape=(120, 120)):
        class_names = os.listdir(folder_path)
        X_train = []
        y_train = []
        
        for i, class_name in enumerate(class_names):
            class_dir = os.path.join(folder_path, class_name)
            for img_name in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_name)
                img = cv2.imread(img_path)
                img = cv2.resize(img, input_shape)  # Resize ảnh về kích thước thích hợp
                X_train.append(img)
                y_train.append(i)

        # for label in os.listdir(folder_path):
        #     label_path = os.path.join(folder_path, label)
        #     for name in os.listdir(label_path):
        #         file_name = os.path.join(label_path, name)
        #         labels = os.listdir(file_name)
        #         for i, label in enumerate(labels):
        #             label_to_index[label] = i
        #         if os.path.isdir(file_name):
        #                 for img_name in os.listdir(file_name):
        #                     img_path = os.path.join(file_name, img_name)
        #                     img = cv2.imread(img_path)
        #                     img = cv2.resize(img, input_shape)
        #                     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #                     img = img.astype('float32') / 255.0
        #                     X_train.append(img)
        #                     y_train.append(name)
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        return X_train, y_train 
    
    def train_model(self, X_train, y_train, epochs=10):
        self.compile_model()
        self.model.fit(X_train, y_train, epochs=epochs)
    
    
    def chuanhoa_label(self, label):
        ch_label = np.array([label])
        return ch_label
    
if __name__ == "__main__":
    data_dir = 'data/khachhang'
    list = os.listdir(data_dir)
    num = len(list)
    model = CNNModel(count=num)
    datax, datay = model.load_data(data_dir)
    model.train_model(datax, datay)
    print(model.predict_img(model.model,'data/khachhang/4/4_16.png'))
    



	