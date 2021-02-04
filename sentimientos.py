import numpy as np
import cv2
from tensorflow.keras.models import load_model

emotion_model_path = '_mini_XCEPTION_5_FER_RAF_CK.hdf5'
model = load_model(emotion_model_path, compile=False)
facecasc = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cont_frame = 0
maxindex=0
print('Comienzo bucle')
emotion_dict = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
while True:
    ret, frame = cap.read()
    cont_frame += 1
    if not ret:
        print("No tengo imagen")
        break
    if cont_frame == 4:
        cont_frame = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:

            cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = model.predict(cropped_img / 255)[0]
            maxindex = int(np.argmax(prediction))

        cv2.putText(frame, emotion_dict[maxindex], (x + 20, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0),
                    2,
                    cv2.LINE_AA)
        cv2.imshow('Video', cv2.resize(frame, (640, 480), interpolation=cv2.INTER_CUBIC))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Me salgo")
        break

print("cap release")
cap.release()
cv2.destroyAllWindows()