import cv2
image=cv2.imread("python-img.jpg",1)
if image is not None:
    print("image loaded successfully")
else:
    print("error:could not load image")
 # 1. Create a resizable window first
cv2.namedWindow("my image", cv2.WINDOW_NORMAL)
    
    # 2. (Optional) Force the window to resize to a manageable preview size
cv2.resizeWindow("my image", 800, 600) 

cv2.imshow("my image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
success=cv2.imwrite("output.jpg",image)
if success:
    print("output image saved successfully")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("my image", cv2.WINDOW_NORMAL)
    
    # 2. (Optional) Force the window to resize to a manageable preview size
cv2.resizeWindow("my image", 800, 600) 
cv2.imshow("my image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()



