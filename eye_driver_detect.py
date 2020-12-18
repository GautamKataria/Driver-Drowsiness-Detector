import cv2
from tensorflow import keras
import numpy as np
new_model = keras.models.load_model('mymodel_drowsiness_custom_final.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    eyes = eye_cascade.detectMultiScale(gray,1.1,4)
    if len(eyes)!= 0:
        for x,y,w,h in eyes:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            eyes1 = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes1) == 0:
                eyes_roi = roi_color

            else:
                for(ex,ey,ew,eh) in eyes1:
                    eyes_roi = roi_color[ey:ey+eh, ex:ex+ew]
        
        final_image = cv2.resize(eyes_roi, (224,224))
        final_image = np.expand_dims(final_image, axis = 0) ## adding 4th dimension
        final_image = final_image/255.0

        predictions = new_model.predict(final_image)
        if (predictions> 0.8):
            status = "open eyes"
            cv2.imshow('eyes', eyes_roi)
            print(predictions)
        elif (predictions < 0.01):
            cv2.imshow('eyes', eyes_roi)
            status= "closed eyes"
            print(predictions)

    else:
        status = "no eye detected"
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    font = cv2.FONT_HERSHEY_SIMPLEX
    try:
        cv2.putText(frame, status, (50,50), font , 2, (0,255,0),3, cv2.LINE_8)
    except Exception as e:
        pass
    cv2.imshow("drowsiiness detection", frame)
    
    if cv2.waitKey(2) &0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWIndows()