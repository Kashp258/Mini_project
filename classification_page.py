import streamlit as st
import openai
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input  # Adjust according to your model

# Set your OpenAI API Key here
openai.api_key = 'sk-xyV8eYbh4ewLxpeGlugXV9NaryEMebUSioxW1qFy3IT3BlbkFJNUCfd-ApmWHgI8xTc-sma6eD4PSePl3kDTokpyvvEA'

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

# Function to get advanced suggestions using OpenAI's model
def get_advanced_suggestions(predicted_label):
    prompt = f"Give detailed, actionable suggestions on how to recycle, reuse, or properly dispose of {predicted_label}. Include environmental benefits and easy-to-follow steps."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    suggestions = response.choices[0].message['content'].strip()
    return suggestions

# Show classification page
def show_classification_page():
    # Set background image and styles
    st.markdown(
        """
        <style>
        body {
            background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #fff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.7);
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1.2em;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #45a049;
        }
        .suggestion {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 8px;
            padding: 10px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title">Waste Classification App</div>', unsafe_allow_html=True)
    st.write("Upload an image of waste to classify it, or use your webcam.")

    model, labels = None, None

    try:
        model = load_model_func()
        st.success("Model loaded successfully!", icon="✅")
    except Exception as e:
        st.error(f"Error loading model: {e}")

    try:
        labels = load_labels()
        st.success("Labels loaded successfully!", icon="✅")
    except Exception as e:
        st.error(f"Error loading labels: {e}")

    # Image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("")
        image_data = preprocess_image(uploaded_file)
        if model and labels:
            predicted_label = classify_image(model, labels, image_data)
            st.write(f"Predicted label: **{predicted_label}**", unsafe_allow_html=True)
            suggestions = get_advanced_suggestions(predicted_label)
            st.subheader("Recycling Suggestions:")
            st.markdown(f'<div class="suggestion">{suggestions}</div>', unsafe_allow_html=True)

    # Webcam capture
    st.write("### or use your webcam to classify waste")
    camera_input = st.camera_input("Take a picture")
    
    if camera_input is not None:
        st.image(camera_input, caption='Captured Image', use_column_width=True)
        st.write("")
        image_data = preprocess_image(camera_input)
        if model and labels:
            predicted_label = classify_image(model, labels, image_data)
            st.write(f"Predicted label: **{predicted_label}**", unsafe_allow_html=True)
            suggestions = get_advanced_suggestions(predicted_label)
            st.subheader("Recycling Suggestions:")
            st.markdown(f'<div class="suggestion">{suggestions}</div>', unsafe_allow_html=True)

# Main application
if __name__ == "__main__":
    show_classification_page()
