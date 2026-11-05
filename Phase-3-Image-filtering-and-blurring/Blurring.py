import cv2
image=cv2.imread("sample.png")
image2=cv2.imread("sample2.png")
resized=cv2.resize(image,(600,600))
if image is None:
    print("Could not load image!")
blurred1=cv2.GaussianBlur(resized,(9,9),0)
blurred2=cv2.medianBlur(image2,9)
cv2.imwrite("gaussianblurred.png",blurred1)
cv2.imwrite("medianblurred.png",blurred2)
cv2.imshow("gaussian blur",blurred1) 
cv2.imshow("median blur",blurred2) 
cv2.waitKey(0)
cv2.destroyAllWindows()   