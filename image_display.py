import cv2
image=cv2.imread("sample-img.png",1)
if image is not None:
    print("image loaded successfully")
    cv2.imshow("my image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error:could not load image")
