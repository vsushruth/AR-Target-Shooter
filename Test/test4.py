import cv2

img = cv2.imread('bookpage.jpg' , 0)
ret, threshold = cv2.threshold(img , 12 , 255 , cv2.THRESH_BINARY)
thresh = cv2.adaptiveThreshold(img, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)

#cv2.destroyAllWindow()


#cv2.imshow('image' , img)
cv2.imshow('Threshold' , threshold)
cv2.imshow('AdThreshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindow()

