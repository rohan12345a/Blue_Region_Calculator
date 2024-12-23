# Blue Region Percentage Calculator

This application calculates the percentage of the blue region in an image using OpenCV and Streamlit. The program automatically detects the lower and upper HSV bounds for the blue color by analyzing a Region of Interest (ROI) in the image.

## Features
- Upload an image and automatically detect the blue region.
- Calculate and display the percentage of blue pixels in the image.
- Visualize the original image and the corresponding blue mask side by side.

## Prerequisites
Before running this application, ensure you have the following Python packages installed:
- `opencv-python`
- `numpy`
- `matplotlib`
- `Pillow`
- `streamlit`

You can install these dependencies by running:

```bash
pip install opencv-python numpy matplotlib Pillow streamlit
