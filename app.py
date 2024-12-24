import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Streamlit app
st.title("Blue Region Percentage Calculator")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded image to a format that OpenCV can handle
    image = np.array(Image.open(uploaded_file))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Defining a Region of Interest (ROI) manually for automatic bounds calculation
    x, y, w, h = 100, 100, 50, 50  # Example ROI (x, y, width, height)
    roi = hsv_image[y:y+h, x:x+w]  # Crop the region

    min_hsv = np.min(roi, axis=(0, 1))
    max_hsv = np.max(roi, axis=(0, 1))

    st.write(f"Lower HSV bound: {min_hsv}")
    st.write(f"Upper HSV bound: {max_hsv}")

    blue_mask = cv2.inRange(hsv_image, min_hsv, max_hsv)

    # Count the number of blue pixels
    blue_pixels = cv2.countNonZero(blue_mask)

    total_pixels = image.shape[0] * image.shape[1]

    blue_percentage = (blue_pixels / total_pixels) * 100

    # Displaying the percentage of blue region
    st.write(f"Percentage of blue region in the image: {blue_percentage:.2f}%")

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[0].set_title("Original Image")
    ax[0].axis('off')

    ax[1].imshow(blue_mask, cmap='gray')
    ax[1].set_title("Blue Mask")
    ax[1].axis('off')

    st.pyplot(fig)

with st.container():
    with st.sidebar:
        members = [
            {"name": "Rohan Saraswat", "email": "rohan.saraswat2003@gmail.com", "linkedin": "https://www.linkedin.com/in/rohan-saraswat-a70a2b225/"},
        ]

        st.markdown("<h1 style='font-size:28px'>Author</h1>", unsafe_allow_html=True)

        for member in members:
            st.write(f"Name: {member['name']}")
            st.write(f"Email: {member['email']}")
            st.write(f"LinkedIn: {member['linkedin']}")
            st.write("")
