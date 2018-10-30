import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True :
        ret, frame = cap.read()
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
		eye_gray = gray[y:y+h, x:x+w]
		eye_orig = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(eye_gray)
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(eye_orig, (ex,ey),(ex+ew , ey+eh),(255,255,0),3)

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


