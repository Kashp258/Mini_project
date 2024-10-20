import streamlit as st
import os
import numpy as np
from PIL import Image
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
import time

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)

# Function to load the model
def load_model_func():
    model_path = 'keras_model.h5'
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    return model

# Load the labels from the labels file
def load_labels():
    labels_path = 'labels.txt'
    if not os.path.isfile(labels_path):
        raise FileNotFoundError(f"Labels file not found: {labels_path}")
    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()
    return labels

# Function to preprocess the uploaded image
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Function to classify an image
def classify_image(model, labels, image_data):
    predictions = model.predict(image_data)
    predicted_label = labels[np.argmax(predictions)]
    return predicted_label

# Function to get recycling suggestions based on the predicted label
def get_suggestions(predicted_label):
    suggestions = {
        "Plastic": [
            "1. Recycle plastic containers by rinsing and placing them in recycling bins.",
            "2. Consider using reusable bags instead of plastic ones.",
            "3. Upcycle plastic bottles into planters or storage containers."
        ],
        "Metal": [
            "1. Clean and recycle metal cans in your local recycling program.",
            "2. Use metal containers for storage instead of plastic.",
            "3. Donate old metal items instead of throwing them away."
        ],
        "Paper": [
            "1. Recycle paper products like newspapers and cardboard.",
            "2. Use both sides of paper before discarding.",
            "3. Shred sensitive documents and recycle the scraps."
        ],
        "Glass": [
            "1. Rinse glass jars and bottles before recycling them.",
            "2. Consider using glass containers for food storage.",
            "3. Repurpose glass jars as vases or decorative items."
        ],
        "Compost": [
            "1. Compost kitchen scraps to create nutrient-rich soil.",
            "2. Use compost bins or piles to reduce waste.",
            "3. Educate others about the benefits of composting."
        ],
        "Cardboard": [
            "1. Flatten cardboard boxes before recycling.",
            "2. Reuse cardboard for crafts or storage.",
            "3. Consider donating cardboard boxes to local schools or charities."
        ]
    }
    return suggestions.get(predicted_label, ["No specific suggestions available."])

# Show classification page
def show_classification_page():
    # Set up the enhanced page style
    st.markdown(
        """
        <style>
        body {
            background-color: #F0FFF0;  /* Light green background for freshness */
            font-family: 'Helvetica', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 3.5em;
            color: #228B22;  /* Bright green */
            font-weight: 700;
            padding: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.4);
        }
        .upload-section, .suggestion {
            background: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin: 15px 0;
        }
        .button {
            background-color: #006400; /* Dark green */
            color: #ffffff;
            padding: 12px 25px;
            font-size: 1.2em;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #32CD32; /* Bright green hover */
        }
        .suggestion {
            margin-top: 20px;
            padding: 15px;
            background-color: rgba(155, 191, 101, 0.8);
            border-radius: 8px;
            font-size: 1.1em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display enhanced title
    st.markdown('<div class="title">Waste Classification App 🌱</div>', unsafe_allow_html=True)
    st.write("### Upload an image to classify the type of waste")

    # Upload section
    uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

    model, labels = None, None
    try:
        model = load_model_func()
        labels = load_labels()
    except Exception as e:
        st.error(f"Error loading model or labels: {e}")

    # Handle image upload
    if uploaded_file is not None:
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("### Result:")

        if st.button("Classify Waste", key="classifyButton", help="Click to classify the waste image"):
            with st.spinner('Classifying... Please wait.'):
                time.sleep(3)
                if model and labels:
                    image_data = preprocess_image(uploaded_file)
                    predicted_label = classify_image(model, labels, image_data)
                    st.success(f"Predicted label: **{predicted_label}**")
                    suggestions = get_suggestions(predicted_label)
                    st.subheader("Recycling Suggestions:")
                    for suggestion in suggestions:
                        st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
                else:
                    st.error("Model or labels not available. Please check.")

        st.markdown('</div>', unsafe_allow_html=True)

    # Enhanced sidebar
    st.sidebar.markdown("## Waste Classification App")
    st.sidebar.write("This application helps you classify types of waste by analyzing images. Learn how you can better manage and recycle waste effectively.")

    # Footer with enhanced links
    st.markdown(
        "<div style='text-align: center; padding-top: 30px;'>"
        "<a href='#' style='color: #32CD32; font-size: 1.1em; text-decoration: none;'>Learn More about Waste Management</a> | "
        "<a href='#' style='color: #32CD32; font-size: 1.1em; text-decoration: none;'>Recycling Tips</a>"
        "</div>",
        unsafe_allow_html=True
    )

# Main application
if __name__ == "__main__":
    show_classification_page()
