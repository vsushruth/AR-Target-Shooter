import cv2
img = cv2.imread('2.jpg' , 1)
cv2.imshow('image' , img)
cv2.imwrite('output.jpg')
