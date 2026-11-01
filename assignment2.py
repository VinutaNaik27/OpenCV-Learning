import cv2
path=input("enter the path of the image:")
image=cv2.imread(path,0)
print("enter 1 if you want to draw a line on the image\n enter 2 if you want to draw a rectangle on the image\n enter 3 if you want to draw a circle on the image\nenter 4 if you want to enter a text on the image\n")