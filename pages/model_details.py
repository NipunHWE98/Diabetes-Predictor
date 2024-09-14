import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Model Comparision", layout="wide")

# Define image paths using forward slashes or raw strings
image1_path = "asserts/table.png"
image2_path = "asserts/cap1.png"
image3_path = "asserts/cap2.png"
image4_path = "asserts/cap3.png"

# Load images with corrected paths
try:
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image3 = Image.open(image3_path)
    image4 = Image.open(image4_path)
except FileNotFoundError as e:
    st.error(f"Error loading image: {e}")
    st.stop()

# Title
st.title("Model Comparision using cross validation")

# Create a single column to display all images
col = st.columns(1)[0]  # Single column

with col:
    st.image(image1, caption='Figure: 1: evaluation', use_column_width=True)
    st.image(image2, caption='Figure: 2', use_column_width=True)
    st.image(image3, caption='Figure: 3', use_column_width=True)
    st.image(image4, caption='Figure: 4', use_column_width=True)
