# Phase 2 – OpenCV Image Processing

## Project Overview

This phase focuses on learning image processing and drawing operations using Python and OpenCV.

The project contains programs to perform different operations on images, including rotation, cropping, resizing, flipping, and drawing geometric shapes.

Users can load an image, perform the required operations, display the modified image, and save the output.

This phase helps in understanding image coordinates, image dimensions, and basic image manipulation techniques.

## Technologies Used

- Python
- OpenCV (cv2)


## Project Structure

```text
Phase-2-Image-Processing/
│
├── assignment2.py
├── assignment3.py
│
├── output_circle.png
├── output_line_drawn.png
├── output_rectangle.png
├── output_text.png
│
├── README.md
└── sample-img.png
```

### File Description

| File | Description |
|---|---|
| `assignment2.py` | Image drawing operations |
| `assignment3.py` | Additional image processing practice |
| `sample-img.png` | Sample image used for testing |
| `output_circle.png` | Image containing a drawn circle |
| `output_line_drawn.png` | Image containing a drawn line |
| `output_rectangle.png` | Image containing a drawn rectangle |
| `output_text.png` | Image containing text |

## Features

### Image Processing

- Load an image using its file path.
- Choose between color and grayscale modes.
- Rotate an image using a specified angle.
- Change the image scale during rotation.
- Crop an image using X and Y coordinates.
- Resize an image to custom dimensions.
- Flip an image horizontally, vertically, or in both directions.
- Display the modified image.
- Save the processed image as a PNG file.

### Image Drawing

- Draw a line between two points.
- Draw a rectangle using two corner points.
- Draw a circle using its center and radius.
- Add custom text to an image.
- Perform multiple drawing operations on the same image.
- Save the modified image.

## OpenCV Functions Used

| Function | Purpose |
|---|---|
| `cv2.imread()` | Reads an image from a file |
| `cv2.getRotationMatrix2D()` | Creates a rotation matrix |
| `cv2.warpAffine()` | Applies rotation and affine transformations |
| `cv2.resize()` | Resizes an image |
| `cv2.flip()` | Flips an image |
| `cv2.line()` | Draws a line |
| `cv2.rectangle()` | Draws a rectangle |
| `cv2.circle()` | Draws a circle |
| `cv2.putText()` | Adds text to an image |
| `cv2.imshow()` | Displays an image |
| `cv2.waitKey()` | Waits for a keyboard event |
| `cv2.destroyAllWindows()` | Closes OpenCV windows |
| `cv2.imwrite()` | Saves an image |

## Installation

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

### 2. Install OpenCV

Open the terminal and execute:

```bash
pip install opencv-python
```

### 3. Clone the Repository

```bash
git clone https://github.com/VinutaNaik27/OpenCV-Learning.git
```

Navigate to the Phase 2 directory:

```bash
cd OpenCV_Learning/Phase-2-Image-Processing
```

## How to Run

Run the drawing assignment:

```bash
python assignment2.py
```

Run the additional assignment:

```bash
python assignment3.py
```

Enter the image path when prompted.

Example:

```text
Enter the path of the image: sample-img.png
```

## Image Coordinate System

OpenCV uses a coordinate system where:

- The origin `(0, 0)` is at the top-left corner.
- The X-axis represents the horizontal direction.
- The Y-axis represents the vertical direction.

The image dimensions are obtained using:

```python
height, width = image.shape[:2]
```

For resizing, OpenCV expects the dimensions in the order:

```python
(width, height)
```

## Learning Outcomes

Through this phase, I learned:

- How to load and display images using OpenCV.
- How to work with image coordinates.
- How to rotate, crop, resize, and flip images.
- How to draw geometric shapes on images.
- How to add text to images.
- How to handle color and grayscale images.
- How to save modified images.
- How to implement menu-driven programs using Python `while` loops and `match-case`.

## Future Improvements

- Add custom color selection for drawing.
- Allow users to change the thickness of shapes.
- Implement undo and reset functionality.
- Add mouse-based drawing.
- Explore image brightness and contrast adjustment.
- Implement edge detection and thresholding.
- Build real-time computer vision applications.

## Author

**Vinuta Naik**

GitHub: [VinutaNaik27](https://github.com/VinutaNaik27)

Repository: [OpenCV-Learning](https://github.com/VinutaNaik27/OpenCV-Learning)
