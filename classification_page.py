import streamlit as st
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input
from PIL import Image
import base64

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

# Function to add a background image
def add_bg_from_url():
    background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{background_image_url}");
             background-size: cover;
             background-repeat: no-repeat;
             background-attachment: fixed;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Function to provide recycling, reusing, or degrading suggestions
def get_suggestions(waste_type):
    suggestions = {
        "Cardboard": [
            "Reuse clean cardboard boxes for storage or shipping.",
            "Recycle cardboard at a local recycling facility.",
            "Avoid soiled cardboard as it may not be accepted for recycling."
        ],
        "Compost": [
            "Add compostable items to a home compost bin.",
            "Use compost as a natural fertilizer for plants.",
            "Ensure only biodegradable items are added to compost."
        ],
        "Glass": [
            "Recycle glass bottles and jars at designated drop-off points.",
            "Reuse glass containers for storage or craft projects.",
            "Avoid mixing glass with other waste to prevent contamination."
        ],
        "Metal": [
            "Recycle aluminum cans and metal scraps at recycling centers.",
            "Repurpose metal items for DIY projects or home repairs.",
            "Separate metals based on type (aluminum, steel, etc.) for efficient recycling."
        ],
        "Paper": [
            "Recycle clean paper products such as newspapers and office paper.",
            "Reuse paper for notes or as wrapping material.",
            "Avoid recycling paper with heavy ink or contamination."
        ],
        "Plastic": [
            "Recycle plastic bottles, containers, and packaging where accepted.",
            "Opt for reusable containers to reduce plastic waste.",
            "Clean and dry plastics before recycling to ensure acceptance."
        ]
    }
    return suggestions.get(waste_type, ["No specific suggestions available."])

# Show classification page
def show_classification_page():
    add_bg_from_url()
    
    # Streamlit app layout
    st.title("🌍 Waste Classification App")
    st.markdown("**Upload an image of waste to get it classified and receive tips on how to recycle, reuse, or dispose of it responsibly.**")
    
    # Load the model and labels
    model = None
    labels = None
    try:
        model = load_model_func()
        labels = load_labels()
    except Exception as e:
        st.error(f"Error: {e}")
        return

    # Image upload
    uploaded_file = st.file_uploader("📤 Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='📸 Uploaded Image', use_column_width=True)
        st.write("✅ Image uploaded successfully!")
        
        if model and labels:
            image_data = preprocess_image(uploaded_file)
            predictions = model.predict(image_data)
            predicted_label = labels[np.argmax(predictions)]
            
            # Display the predicted label
            st.markdown(f"### 🏷️ Predicted Label: **{predicted_label.capitalize()}**")
            
            # Get and display recycling/reusing/degrading suggestions
            suggestions = get_suggestions(predicted_label)
            st.markdown("### ♻️ **Suggestions for Recycling/Reuse/Degrading:**")
            for idx, suggestion in enumerate(suggestions, start=1):
                st.markdown(f"- {suggestion}")
        else:
            st.error("Model or labels not available. Please check if they were loaded correctly.")

# Run the app
if __name__ == "__main__":
    show_classification_page()
