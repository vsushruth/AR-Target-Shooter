import cv2
import numpy as np

img = cv2.imread('2.jpg',1)
#cv2.imshow("image",img)

cv2.rectangle(img,(0, 0),(400,500),(255,0,0),2)
cv2.imshow('edited' , img)

cv2.circle(img,(500,500),50,(0,0,255),1)
cv2.imshow('edited' , img)

pts = np.array([[100 ,200],[400,500],[350,406],[347,567]], np.int32)
cv2.polylines(img, [pts], False , (255,123,7) , 2)
cv2.imshow('edited' , img)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ABCD' , (200,200) ,font, 1,(125,255,125), 2, cv2.LINE_AA)
cv2.imshow('edited' , img)


cv2.waitKey(0)
cv2.destroyAllWindow()
