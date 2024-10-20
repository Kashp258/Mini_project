import streamlit as st
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input  # Adjust according to your model
from PIL import Image
import time

# Custom DepthwiseConv2D class to handle loading without 'groups' argument
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop('groups', None)
        super().__init__(*args, **kwargs)

# Function to load the model
def load_model_func():
    model_path = 'keras_model.h5'  # or provide the absolute path
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    
    model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D})
    return model

# Load the labels from the labels file
def load_labels():
    labels_path = 'labels.txt'  # or provide the absolute path
    if not os.path.isfile(labels_path):
        raise FileNotFoundError(f"Labels file not found: {labels_path}")

    with open(labels_path, 'r') as file:
        labels = file.read().splitlines()
    return labels

# Function to preprocess the uploaded image
def preprocess_image(img_file):
    img = image.load_img(img_file, target_size=(224, 224))  # Adjust according to your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)  # Preprocess for your model (e.g., MobileNetV2)
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
    st.markdown(
        """
        <style>
        body {
            background-color: #EBF2B3; /* Light Green background */
            color: #1B4001;  /* Dark Green text */
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 3em;
            color: #1B4001;  /* Dark Green */
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
            padding: 15px 0;
        }
        .button {
            background-color: #3B7302; /* Medium Dark Green */
            color: #EBF2B3; /* Light Green */
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2em;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #65A603; /* Bright Green */
        }
        .suggestion {
            background-color: rgba(155, 191, 101, 0.8); /* Soft Green */
            border-radius: 8px;
            padding: 15px;
            margin-top: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
        }
        .upload-section, .camera-section {
            background-color: #F5F8E6; /* Very Light Green */
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Waste Classification App 🌎</div>', unsafe_allow_html=True)

    option = st.radio("Choose input method:", ("Upload Image", "Use Webcam"))

    model, labels = None, None
    try:
        model = load_model_func()
        labels = load_labels()
    except Exception as e:
        st.error(f"Error loading resources: {e}")

    if option == "Upload Image":
        st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
            image_data = preprocess_image(uploaded_file)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"### Result: **{predicted_label}**")
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if option == "Use Webcam":
        st.markdown("<div class='camera-section'>", unsafe_allow_html=True)
        st.write("### Capture an Image Using Your Webcam")
        camera_input = st.camera_input("Take a picture")
        if camera_input is not None:
            img = Image.open(camera_input)
            st.image(img, caption='Captured Image', use_column_width=True)
            image_data = preprocess_image(camera_input)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"### Result: **{predicted_label}**")
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    show_classification_page()
