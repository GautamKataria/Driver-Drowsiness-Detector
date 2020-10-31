import cv2
import numpy as np

if not os.path.exists('Images'):
	print("New directory created")
	os.makedirs('Images')

cap = cv2.VideoCapture(0)
n=0
while True:
    ret, frame = cap.read()
    if (n < 100):
        cv2.imshow('cam', frame)
        file_name_path = './Images/' + str(n) + '.jpg'
        cv2.imwrite(file_name_path, frame)
        n = n+1
    if cv2.waitKey(1) == 13 or n == 100:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Complete")