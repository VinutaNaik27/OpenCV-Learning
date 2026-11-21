import cv2
import numpy as np
image=cv2.imread("sharpen_sample.png")
if image is None:
    print("could not load image!")
sharpen_kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float32)
sharpen=cv2.filter2D(image,-1,sharpen_kernel)
sharpened=cv2.resize(sharpen,(600,600))
cv2.imwrite("sharpened.png",sharpened)
cv2.imshow("blurred image",image)
cv2.imshow("Sharpened image",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Original image:", image is None)

