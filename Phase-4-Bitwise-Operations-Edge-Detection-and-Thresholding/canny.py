import cv2
image=cv2.imread("canny_sample.png",cv2.IMREAD_GRAYSCALE)

if image is None:
    print("could not load image")

else:
    edges=cv2.Canny(image,50,180)
    cv2.imwrite("canny_output.png",edges)
    cv2.imshow("Canny edge detection",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()