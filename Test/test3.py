import cv2

img = cv2.imread('2.jpg' , 1)
#print(img[225,600])
img[225,600] = (255,255,255)
#print(img[225,600])

img[100:155,100:155] = (255,255,255)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindow()

