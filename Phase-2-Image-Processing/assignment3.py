import cv2
path = input("Enter the path of the image: ")
col_or_gray = int(input(
    "Enter 1 for color image or 0 for grayscale image: "
))

if col_or_gray == 1:
    image = cv2.imread(path, cv2.IMREAD_COLOR)
elif col_or_gray == 0:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
else:
    print("Invalid image type!")
    exit()
if image is None:
    print("Error: Image not found!")
    exit()

height, width = image.shape[:2]

while True:
    print("""
    1. Rotate the image
    2. Crop the image
    3. Resize the image
    4. Flip the image
    """)

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            centre = (width // 2, height // 2)
            angle = float(input("Enter the angle of rotation: "))
            scale = float(input("Enter scale (1 for same size, 2 for double, 0.5 for half): "))
            M = cv2.getRotationMatrix2D(
                centre, angle, scale
            )
            output = cv2.warpAffine(image, M, (width, height))
            filename = "rotated.png"
            break
        case 2:
            Ystart, Yend = map(int,input("Enter starting and ending Y coordinates: ").split(','))
            Xstart, Xend = map(int,input("Enter starting and ending X coordinates: ").split(','))
            output = image[Ystart:Yend, Xstart:Xend]
            if output.size == 0:
                print("Invalid cropping coordinates!")
                continue
            filename = "cropped.png"
            break
        case 3:
            (w, h) =image.shape[:]
            if w <= 0 or h <= 0:
                print("Width and height must be positive!")
            output = cv2.resize(image, (w, h))
            filename = "resized.png"
            break
        case 4:
            flip_code = int(input("Enter flip code (0: vertical, 1: horizontal, -1: both): "))
            if flip_code not in [0, 1, -1]:
                print("Invalid flip code!")
                continue
            output = cv2.flip(image, flip_code)
            filename = "flipped.png"
            break
        case _:
            print("Invalid choice! Please try again.")
            continue
cv2.imshow("Modified Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

ch = int(input(
    "Enter 1 if you want to save the image: "
))

if ch == 1:
    cv2.imwrite(filename, output)
    print("Image saved successfully:", filename)
else:
    print("Image not saved.")
