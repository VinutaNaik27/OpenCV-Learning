# 👁️ OpenCV Learning Journey 🚀

## Project Overview

Welcome to my OpenCV Learning Repository!

This repository documents my journey of learning Computer Vision using Python and OpenCV. It contains practical programs, assignments, and experiments covering different concepts of image processing and computer vision.

I am following a phase-wise approach to understand OpenCV concepts, practice them through Python programs, and gradually build a foundation for real-world computer vision applications.

## Progress Tracker

| Phase | Topic | Status |
|---|---|---|
| Phase 1 | OpenCV Basics | ✅ Completed |
| Phase 2 | Image Processing | ✅ Completed |
| Phase 3 | Image Filtering, Blurring and Sharpening | ✅ Completed |
| Phase 4 | Bitwise Operations, Edge Detection and Thresholding | ✅ Completed |
| Phase 5 | Webcam video|🚧 In Progress|
## Technologies Used

- Python
- OpenCV (cv2)
- NumPy
- Git and GitHub

## Repository Structure

```text
OpenCV-Learning/
│
├── Phase-1-Basics/
│   ├── image_read.py
│   ├── image_display.py
│   ├── image_save.py
│   ├── assignment1.py
│   └── sample and output images
│
├── Phase-2-Image-Processing/
│   ├── assignment2.py
│   ├── assignment3.py
│   ├── sample-img.png
│   └── output images
│
├── Phase-3-Image-filtering-and-blurring/
│   ├── Blurring.py
│   ├── sharpening.py
│   └── sample and output images
│
├── Phase-4-edge-detection-and-thresholding/
│   ├── Bitwise_operations.py
│   ├── canny.py
│   ├── thresh.py
│   └── input and output images
│
├── README.md
└── .gitignore
```

## Learning Phases

### Phase 1 – OpenCV Basics

**Programs:** `image_read.py`, `image_display.py`, `image_save.py`, `assignment1.py`

**Topics Covered:**

- Introduction to OpenCV.
- Reading and displaying images.
- Understanding image properties.
- Working with color and grayscale images.
- Saving images.
- Basic image operations.

### Phase 2 – OpenCV Image Processing

**Programs:** `assignment2.py`, `assignment3.py`

**Topics Covered:**

- Image rotation.
- Image cropping.
- Image resizing.
- Image flipping.
- Drawing lines, rectangles, and circles.
- Adding text to images.
- Understanding image coordinates.
- Working with color and grayscale images.

### Phase 3 – Image Filtering, Blurring and Sharpening

**Programs:** `Blurring.py`, `sharpening.py`

**Topics Covered:**

- Introduction to image filtering.
- Gaussian Blur using `cv2.GaussianBlur()`.
- Median Blur using `cv2.medianBlur()`.
- Understanding image smoothing and noise reduction.
- Image sharpening using custom kernels.
- Unsharp masking.
- Applying convolution using `cv2.filter2D()`.
- Comparing blurred and sharpened images.

**Key Learnings:**

- Gaussian blur works well for Gaussian noise, while median blur works better for salt-and-pepper noise.
- A larger (odd-sized) kernel gives a stronger blur.
- Sharpening kernels boost existing edges and help enhance image details.
- Heavy blur cannot be fully recovered by sharpening because the lost details cannot be completely restored.

### Phase 4 – Bitwise Operations, Edge Detection and Thresholding

**Programs:** `Bitwise_operations.py`, `canny.py`, `thresh.py`

**Topics Covered:**

**1. Bitwise Operations**

- Understanding bitwise operations in OpenCV.
- Creating binary images using NumPy.
- Performing Bitwise AND using `cv2.bitwise_and()`.
- Performing Bitwise OR using `cv2.bitwise_or()`.
- Performing Bitwise NOT using `cv2.bitwise_not()`.
- Understanding how bitwise operations work with image masks.

**2. Canny Edge Detection**

- Introduction to edge detection.
- Understanding the importance of edges in computer vision.
- Detecting edges using `cv2.Canny()`.
- Understanding how Canny edge detection identifies boundaries and important features in an image.

**3. Image Thresholding**

- Introduction to image thresholding.
- Understanding binary image conversion.
- Applying thresholding using `cv2.threshold()`.
- Understanding how threshold values affect the output image.

**Key Learnings:**

- Bitwise AND returns the common white regions between two binary images.
- Bitwise OR combines the white regions from both images.
- Bitwise NOT inverts the pixel values of an image.
- Canny edge detection helps identify object boundaries and edges.
- Thresholding converts grayscale images into binary images based on a specified threshold value.

## Installation and Setup

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

### 2. Clone the Repository

```bash
git clone https://github.com/VinutaNaik27/OpenCV-Learning.git
```

### 3. Navigate to the Project Directory

```bash
cd OpenCV-Learning
```

### 4. Install Required Libraries

```bash
pip install opencv-python numpy
```

## How to Run the Programs

Navigate to the required phase directory.

For example, to run Phase 4:

```bash
cd Phase-4-edge-detection-and-thresholding
```

Run the Python programs:

```bash
python Bitwise_operations.py
python canny.py
python thresh.py
```

**Note:** The Python file and image paths may vary depending on the program. Run each script from inside its own folder so that the input images are found.

## Learning Objectives

Through this repository, I aim to:

- Understand the fundamentals of computer vision.
- Gain practical experience with OpenCV.
- Learn different image processing techniques.
- Understand how images are represented and manipulated.
- Develop problem-solving and Python programming skills.
- Build a foundation for face detection, object detection, and other computer vision applications.

## Future Goals

- Explore contour detection.
- Learn image segmentation.
- Understand morphological operations.
- Implement face detection using Haar Cascades.
- Explore object detection.
- Work with video processing.
- Build practical computer vision projects.

## Author

**Vinuta Naik**

- GitHub: https://github.com/VinutaNaik27
- Repository: https://github.com/VinutaNaik27/OpenCV-Learning

⭐ This repository is a continuous learning journey. More concepts, experiments, and projects will be added as I explore OpenCV and Computer Vision.
