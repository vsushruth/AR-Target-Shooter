import cv2

cap = cv2.VideoCapture(0)
#fourcc



while True :
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#out.write(frame)
	cv2.imshow('gray' , gray)
	if cv2.waitKey(0) & 0xFF == ord('q') :
		break

cap.release()
cv2.destroyAllWindows()


#if cv2.waitKey(0) & 0xFF == ord('q') :
#	cv2.destroyAllWindows()
