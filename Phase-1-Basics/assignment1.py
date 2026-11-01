import cv2

path = input("Enter the path of the image: ")

col_or_gray = int(input("Enter 1 for colorful image or 0 for grayscale: "))
image = cv2.imread(path, col_or_gray)
if image is not None:

    print("Enter 1 if you want to display image")
    print("Enter 2 if you want to save the image")

    choice = int(input("Enter the choice (1 or 2): "))

    if choice == 1:
        
        cv2.imshow("My Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 2:

       
        success = cv2.imwrite("assignment_output_image.png", image)

        if success:
            print("Image saved successfully as output_image.png")
        else:
            print("ERROR: Unable to save image!")

    else:
        print("Invalid choice!")

else:
    print("ERROR: Image not found!")