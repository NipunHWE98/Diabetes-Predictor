import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Model Comparision", layout="wide")

# Define image paths using forward slashes or raw strings
image1_path = "asserts/fs3.png"
image2_path = "asserts/fs2.png"
image3_path = "asserts/fs1.png"


# Load images with corrected paths
try:
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    image3 = Image.open(image3_path)

except FileNotFoundError as e:
    st.error(f"Error loading image: {e}")
    st.stop()

# Title
st.title("Model Comparision using cross validation")

# Create a single column to display all images
col = st.columns(1)[0]  # Single column

with col:
    st.image(image1, caption='Figure: 1: correlation matrix ', use_column_width=True)
    st.image(image2, caption='Figure: 2: RFE', use_column_width=True)
    st.image(image3, caption='Figure: 3: Feature importance', use_column_width=True)

