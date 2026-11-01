import cv2
image=cv2.imread("sample-img.png",1)
if image is not None:
    print("image loaded successfully")
else:
    print("error:could not load image")