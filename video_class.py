import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PyQt5.QtCore import QThread
class Video(QThread):
    def __init__(self):
        super().__init__()
        self.prediction = []
        
    def run (self):
        emotion_model_path = '_mini_XCEPTION_5_FER_RAF_CK.hdf5'
        model = load_model(emotion_model_path, compile=False)
        facecasc = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        cont_frame=0
        print('Comienzo bucle')  
        while True:
            ret, frame = cap.read()
            cont_frame+=1
            if not ret:
                print("No tengo imange")
                break
            if cont_frame==4:
                cont_frame=0
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    print("Tengo cara")
                    roi_gray = gray[y:y + h, x:x + w]
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                    self.prediction = model.predict(cropped_img/255)[0]
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()