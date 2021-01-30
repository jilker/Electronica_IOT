import numpy as np
import cv2
from tensorflow.keras.models import load_model
import os
import time
from PyQt5.QtCore import pyqtSignal, QThread
class Video(QThread):
    """
    Hilo dedicado a las mediciones en tiempo real.
    """
    def __init__(self):
        self.sentimientos = pyqtSignal(list)
        self.prediction = []
    def run (self):
        emotion_model_path = '_mini_XCEPTION_5_FER_RAF_CK.hdf5'
        model = load_model(emotion_model_path, compile=False)

        num_emotions=5
        emotion_dict = {0: "Neutral", 1: "Felicidad", 2: "Sorpresa", 3: "Tristeza", 4: "Enfado"}
        list_emotion = {"Neutral":0 , "Felicidad":0 , "Sorpresa":0 , "Tristeza":0 , "Enfado":0}
        facecasc = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        cont=0
        cont_frame=0   
        while True:
            ret, frame = cap.read()
            cont_frame+=1
            if not ret:
                break
            if cont_frame==4:
                cont_frame=0
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                #canvas = np.zeros((250, 300, 3), dtype="uint8")
                for (x, y, w, h) in faces:
                    #cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                    cont += 1
                    roi_gray = gray[y:y + h, x:x + w]
                    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                    tic=time.perf_counter()
                    self.prediction = model.predict(cropped_img/255)[0]
                    toc=time.perf_counter()
                    self.sentimientos.emit([self.prediction])
                    print(f"Predicción {toc-tic:0.4f}seconds")
        #             maxindex = int(np.argmax(prediction))
        #             list_emotion[emotion_dict.get(maxindex)]+=1
        #             if prediction[0]<=0.9:
        #                 prediction[0]=0
        #                 maxindex = int(np.argmax(prediction))
        #                 list_emotion[emotion_dict.get(maxindex)]+=1
        #             else:
        #                 maxindex = int(np.argmax(prediction))
        #                 list_emotion[emotion_dict.get(maxindex)]+=1
                    if cont==20:
                        print(list_emotion.values())
                        cont=0        
                    #cv2.putText(frame, emotion_dict[maxindex], (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
                    """for (i, (emotion, prob)) in enumerate(zip(emotion_dict.values(), prediction)):
                        # construct the label text
                        text = "{}: {:.2f}%".format(emotion, prob * 100)

                        # draw the label + probability bar on the canvas
                        # emoji_face = feelings_faces[np.argmax(preds)]

                        w = int(prob * 300)
                        cv2.rectangle(canvas, (7, (i * 35) + 5),
                                    (w, (i * 35) + 35), (0, 0, 255), -1)
                        cv2.putText(canvas, text, (10, (i * 35) + 23),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                                    (255, 255, 255), 2)"""

            #cv2.imshow('Video', cv2.resize(frame, (640,480), interpolation=cv2.INTER_CUBIC))
                #cv2.imshow("Probabilities", canvas)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
