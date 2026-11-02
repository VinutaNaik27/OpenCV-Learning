import cv2
path = input("Enter the path of the image: ")

col_or_gray = int(input(
    "Enter 1 for color image or 0 for grayscale image: "
))
if col_or_gray == 1:
    image = cv2.imread(path, cv2.IMREAD_COLOR)
else:
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)


if image is None:
    print("Error: Image not found!")
    exit()

if col_or_gray == 1:
    color = (255, 0, 0)
else:
    color = 255

print("""
1. Draw a line
2. Draw a rectangle
3. Draw a circle
4. Add text
""")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("Enter coordinates for the line")

        x1, y1 = map(int, input("Enter p1: ").split(","))
        x2, y2 = map(int, input("Enter p2: ").split(","))

        line_on_image = cv2.line(
            image, (x1, y1), (x2, y2), color, 2
        )

        output = line_on_image
        filename = "output_line.png"

    case 2:
        print("Enter top-left and bottom-right coordinates")

        x1, y1 = map(int, input("Enter p1: ").split(","))
        x2, y2 = map(int, input("Enter p2: ").split(","))

        rectangle_on_image = cv2.rectangle(
            image, (x1, y1), (x2, y2), color, 2
        )

        output = rectangle_on_image
        filename = "output_rectangle.png"

    case 3:
        print("Enter the center coordinates")

        x1, y1 = map(int, input("Enter center: ").split(","))

        radius = int(input("Enter the radius: "))

        circle_on_image = cv2.circle(
            image, (x1, y1), radius, color, 2
        )

        output = circle_on_image
        filename = "output_circle.png"

    case 4:
        print("Enter the coordinates")

        x1, y1 = map(int, input("Enter p1: ").split(","))

        text = input("Enter the text: ")

        text_on_image = cv2.putText(
            image,
            text,
            (x1, y1),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            color,
            2
        )

        output = text_on_image
        filename = "output_text.png"

    case _:
        print("INVALID CHOICE!!!!")
        exit()

cv2.imshow("Modified Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()


ch = int(input("Enter 1 if you want to save the image: "))

if ch == 1:
    cv2.imwrite(filename, output)
    print("Image saved successfully:", filename)
else:
    print("Image not saved.")