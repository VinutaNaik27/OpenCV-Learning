import cv2
image=cv2.imread("canny_sample.png",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("could not load image")

else:
    ret,thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

    cv2.imwrite("thresh_output.png",thresh)
    cv2.imshow("Thresholding image",thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
