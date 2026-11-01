# Phase 1: Basic Image Operations using OpenCV

## About the Project

This project is part of my journey in learning Python and OpenCV.

In Phase 1, I learned the basic operations of image processing, such as reading, displaying, and saving images using the OpenCV library.

The programs also demonstrate how to load images in color or grayscale.

## Technologies Used

- Python
- OpenCV (cv2)

## Installation

Install the required OpenCV library:

```bash
pip install opencv-python
```

## Programs Included

### 1. Image Reading (`image_read.py`)

- Reads an image from a specified file path.
- Checks whether the image is loaded successfully.
- Displays a success or error message.

### 2. Image Displaying (`image_display.py`)

- Reads an image using OpenCV.
- Displays the image in a separate window.
- Uses `cv2.waitKey()` to wait for a key press.
- Closes the image window using `cv2.destroyAllWindows()`.

### 3. Image Saving (`image_save.py`)

- Reads an image from a file.
- Saves the image using `cv2.imwrite()`.
- Checks whether the image is saved successfully.

### 4. Image Reading, Displaying, and Saving (`assignment1.py`)

- Takes the image path from the user.
- Allows the user to select color or grayscale mode.
- Provides options to display or save the image.
- Handles image loading and saving errors.

## How to Run

Run any Python program using:

```bash
python image_read.py
```

For displaying an image:

```bash
python image_display.py
```

For saving an image:

```bash
python image_save.py
```

For the combined program:

```bash
python assignment1.py
```

## Sample Image

The project uses a sample butterfly image to demonstrate image reading, displaying, and saving operations.

## What I Learned

- Importing and using the OpenCV library.
- Reading images using `cv2.imread()`.
- Understanding color and grayscale images.
- Displaying images using `cv2.imshow()`.
- Saving images using `cv2.imwrite()`.
- Handling image loading errors.
- Understanding basic image processing operations.

## Future Learning

This is the first phase of my OpenCV learning journey. I will continue exploring more image processing techniques in the upcoming phases.

## Author

**Vinuta Naik**

GitHub: [VinutaNaik27](https://github.com/VinutaNaik27)