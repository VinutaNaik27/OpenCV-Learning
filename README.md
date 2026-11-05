# OpenCV Learning Journey 🚀

## Project Overview

Welcome to my OpenCV Learning Repository!

This repository documents my journey of learning Computer Vision using Python and OpenCV. It contains practical programs, assignments, and experiments covering different concepts of image processing and computer vision.

I am following a phase-wise approach to understand OpenCV concepts, practice them through Python programs, and gradually build a foundation for real-world computer vision applications.

## Progress Tracker

| Phase | Topic | Status |
|-------|-------|--------|
| Phase 1 | OpenCV Basics | ✅ Completed |
| Phase 2 | Image Processing | ✅ Completed |
| Phase 3 | Image Filtering, Blurring and Sharpening | ✅ Completed |
| Phase 4 | Coming soon | 🚧 Upcoming |

## Technologies Used

* Python
* OpenCV (cv2)
* NumPy
* Git and GitHub

## Repository Structure

```
OpenCV-Learning/
│
├── Phase-1-Basics/
│   ├── image_read.py
│   ├── image_display.py
│   ├── image_save.py
│   ├── assignment1.py
│   ├── sample-img.png
│   └── output.png, assignment_output_image.png
│
├── Phase-2-Image-Processing/
│   ├── assignment2.py
│   ├── assignment3.py
│   ├── sample-img.png
│   └── output_circle.png, output_line_drawn.png,
│       output_rectangle.png, output_text.png
│
├── Phase-3-Image-filtering-and-blurring/
│   ├── Blurring.py
│   ├── sharpening.py
│   ├── sample.png, sample2.png, sharpen_sample.png
│   └── gaussianblurred.png, medianblurred.png, sharpened.jpg
│
├── Phase-4/
│   └── Upcoming programs
│
├── README.md
└── .gitignore
```

## Learning Phases

### Phase 1 – OpenCV Basics

**Programs:** `image_read.py`, `image_display.py`, `image_save.py`, `assignment1.py`

**Topics Covered:**

* Introduction to OpenCV.
* Reading and displaying images.
* Understanding image properties.
* Working with color and grayscale images.
* Saving images.
* Basic image operations.

### Phase 2 – OpenCV Image Processing

**Programs:** `assignment2.py`, `assignment3.py`

**Topics Covered:**

* Image rotation.
* Image cropping.
* Image resizing.
* Image flipping.
* Drawing lines, rectangles, and circles.
* Adding text to images.
* Understanding image coordinates.
* Working with color and grayscale images.

### Phase 3 – Image Filtering, Blurring and Sharpening

**Programs:** `Blurring.py`, `sharpening.py`

**Topics Covered:**

* Introduction to image filtering.
* Gaussian Blur using `cv2.GaussianBlur()`.
* Median Blur using `cv2.medianBlur()`.
* Understanding image smoothing and noise reduction.
* Image sharpening using custom kernels.
* Unsharp masking.
* Applying convolution using `cv2.filter2D()`.
* Comparing blurred and sharpened images.

**Key Learnings:**

* Gaussian blur works well for Gaussian noise, while median blur works better for salt-and-pepper noise.
* A larger (odd-sized) kernel gives a stronger blur.
* Sharpening kernels such as `[[0,-1,0],[-1,5,-1],[0,-1,0]]` boost existing edges, so they work best on mildly blurred images.
* Heavy blur cannot be fully recovered by sharpening, because the lost detail is gone. Unsharp masking gives better results but can create halos around edges.

### Phase 4 – Coming Soon 🚧

More OpenCV concepts and practical implementations will be added as I progress in my learning journey.

## Installation and Setup

### 1. Install Python

Download Python from: https://www.python.org/downloads/

### 2. Clone the Repository

```
git clone https://github.com/VinutaNaik27/OpenCV-Learning.git
```

### 3. Navigate to the Project Directory

```
cd OpenCV-Learning
```

### 4. Install Required Libraries

```
pip install opencv-python numpy
```

## How to Run the Programs

Navigate to the required phase directory. For example, to run Phase 3:

```
cd Phase-3-Image-filtering-and-blurring
```

Run the Python programs:

```
python Blurring.py
python sharpening.py
```

**Note:** The Python file and image paths may vary depending on the program. Run each script from inside its own folder so that the input images are found.

## Learning Objectives

Through this repository, I aim to:

* Understand the fundamentals of computer vision.
* Gain practical experience with OpenCV.
* Learn different image processing techniques.
* Understand how images are represented and manipulated.
* Develop problem-solving and Python programming skills.
* Build a foundation for face detection, object detection, and other computer vision applications.

## Future Goals

* Explore image thresholding and edge detection.
* Learn contour detection.
* Understand image segmentation.
* Implement face detection.
* Explore object detection.
* Build practical computer vision projects.

## Author

**Vinuta Naik**

* GitHub: https://github.com/VinutaNaik27
* Repository: https://github.com/VinutaNaik27/OpenCV-Learning

⭐ This repository is a continuous learning journey. More concepts, experiments, and projects will be added as I explore OpenCV and Computer Vision.
