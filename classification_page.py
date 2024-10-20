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
        kwargs.pop('groups', None)  # Remove unsupported 'groups' argument if present
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
def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(224, 224))  # Adjust according to your model's input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
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
    # Set the color palette
    DARK_GREEN = "#1B4001"
    MID_GREEN = "#3B7302"
    BRIGHT_GREEN = "#65A603"
    LIGHT_GREEN = "#9BBF65"
    SOFT_YELLOW = "#EBF2B3"
    
    # Customize the page style
    st.markdown(
        f"""
        <style>
        body {{
            background-color: {SOFT_YELLOW};
        }}
        .sidebar .sidebar-content {{
            background-color: {LIGHT_GREEN};
        }}
        .stButton>button {{
            background-color: {MID_GREEN};
            color: white;
            font-size: 16px;
            border: 1px solid {DARK_GREEN};
            border-radius: 8px;
            transition: background-color 0.3s ease;
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: {DARK_GREEN};
        }}
        .title h1 {{
            font-size: 40px;
            color: {BRIGHT_GREEN};
            font-weight: bold;
            text-align: center;
            padding-top: 10px;
        }}
        .upload-success {{
            color: {MID_GREEN};
            font-weight: bold;
            font-size: 20px;
        }}
        .content-section {{
            background-color: {LIGHT_GREEN};
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit app layout
    st.markdown('<div class="title"><h1>Waste Classification App</h1></div>', unsafe_allow_html=True)
    st.write("Select an option to classify waste:")

    # Add radio button for choosing the input method
    option = st.radio("Choose input method:", ("Upload Image", "Use Webcam"))

    # Load the model and labels when the app starts
    model, labels = None, None
    try:
        model = load_model_func()
    except Exception as e:
        st.error(f"Error loading model: {e}")

    try:
        labels = load_labels()
    except Exception as e:
        st.error(f"Error loading labels: {e}")

    # Handle image upload
    if option == "Upload Image":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Display uploaded image and notify user
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image', use_column_width=True)
            st.toast("Image uploaded successfully! 🎉", icon="✅", duration=3)

            # Preprocess the image and make predictions using the model
            image_data = preprocess_image(uploaded_file)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"Classification Result: **{predicted_label}**")

                # Display recycling suggestions
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)

    # Handle webcam capture
    if option == "Use Webcam":
        st.write("### Use your webcam to classify waste")
        camera_input = st.camera_input("Take a picture")
        
        if camera_input is not None:
            st.image(camera_input, caption='Captured Image', use_column_width=True)
            image_data = preprocess_image(camera_input)
            if model and labels:
                predicted_label = classify_image(model, labels, image_data)
                st.write(f"Classification Result: **{predicted_label}**")

                # Display recycling suggestions
                suggestions = get_suggestions(predicted_label)
                st.subheader("Recycling Suggestions:")
                for suggestion in suggestions:
                    st.markdown(f'<div class="suggestion">{suggestion}</div>', unsafe_allow_html=True)

# Main application
if __name__ == "__main__":
    show_classification_page()
