
import numpy as np
import cv2
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten,Dropout
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import os


class CNNModel:
    def __init__(self, num_class = 1, input_shape=(120, 120, 3)):
        self.input_shape = input_shape
        self.num_class = num_class
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Conv2D(16, (3,3), activation='relu', input_shape=self.input_shape))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Conv2D(32, (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Conv2D(64, (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Conv2D(32, (3,3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dense(self.num_class, activation='sigmoid'))
        return model

    def compile_model(self):
        self.model.compile(optimizer='adam',
                      loss=keras.losses.BinaryCrossentropy(),
                      metrics=['accuracy'])
        
    def save_model(self, path):
        self.model.save(path)
    
    def predict_img(self, img):
        # img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (120, 120))
        img = np.expand_dims(img, axis=0)
        # return img
        return self.model.predict(img)
        
    def load_data(self,folder_path, input_shape=(120,120)):
        class_names = os.listdir(folder_path)
        X_train = []
        y_train = []
        
        for i, class_name in enumerate(class_names):
            class_dir = os.path.join(folder_path, class_name)
            for img_name in os.listdir(class_dir):
                img_path = os.path.join(class_dir, img_name)
                img = cv2.imread(img_path)
                img = cv2.resize(img, input_shape) 
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                X_train.append(img)
                y_train.append(i)
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        # return X_train, y_train 
        label_encoder = LabelEncoder()
        y_train_encoded = label_encoder.fit_transform(y_train)
        y_train_categorical = to_categorical(y_train_encoded)
        
        return X_train, y_train_categorical
    
    def train_model(self, X_train, y_train, epochs=15):
        self.compile_model()
        self.model.fit(X_train, y_train, epochs=epochs)
    
    
if __name__ == "__main__":
    data_dir = 'data/khachhang'
    list = os.listdir(data_dir)
    num = len(list)
    model = CNNModel(num_class=num)
    datax, datay = model.load_data(data_dir)
    print (datay)
    model.train_model(datax, datay)
    model.save_model("model/demo1.h5")
    
    



	