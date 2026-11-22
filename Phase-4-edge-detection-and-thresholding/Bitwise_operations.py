import numpy as np
import cv2
img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")
cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)
bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_not=cv2.bitwise_not(img1)
cv2.imwrite("bitwise_and.png", bit_and)
cv2.imwrite("bitwise_or.png", bit_or)
cv2.imwrite("bitwise_not.png", bit_not)

cv2.imshow("Bitwise AND",bit_and)
cv2.imshow("Bitwise OR",bit_or)
cv2.imshow("Bitwise NOT",bit_not)
cv2.waitKey(0)
cv2.destroyAllWindows()