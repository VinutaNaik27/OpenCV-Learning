import cv2
image=cv2.imread("sample-img.png",1)
if image is not None:
    print("image loaded successfully")
success=cv2.imwrite("output.png",image)
if success:
    print("output image saved successfully as output.png")
else:
    print("ERROR:In saving the image")