import streamlit as st
import numpy as np
import os
from PIL import Image, ImageOps
from keras.models import load_model
import gdown

# Background image URL
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"

# URL to the .h5 model file (direct download link)
model_url = "https://drive.google.com/uc?id=1v2vEY_34pVY_x37eSFKYaT8E4cJ2LwcW"
model_path = "./weights/keras_model.h5"

# Function to download the model if it doesn't exist
def download_model():
    if not os.path.exists(model_path):
        st.write("Downloading model from Google Drive...")
        os.makedirs('./weights', exist_ok=True)
        gdown.download(model_url, model_path, quiet=False)
    else:
        st.write("Model already exists locally.")

# Download model on startup
download_model()

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_teachable_model():
    model = load_model(model_path, compile=False)
    return model

# Load the model
model = load_teachable_model()

# Function to load class labels
def load_labels():
    labels_path = './weights/labels.txt'  # Ensure this file is in your repository
    if os.path.exists(labels_path):
        with open(labels_path, "r") as file:
            labels = file.readlines()
        labels = [label.strip() for label in labels]
        return labels
    else:
        st.error("Labels file not found!")
        return []

class_names = load_labels()

# Preprocessing function to make the image ready for the model
def preprocess_image(image):
    size = (224, 224)  # Size used by Teachable Machine
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

# Custom CSS for background image
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        font-family: 'Arial', sans-serif;
    }}
    .header-title {{
        color: #1a1a1a;
        font-size: 28px;
        font-weight: bold;
    }}
    p, ul {{
        color: #1a1a1a;
    }}
    .step {{
        background-color: #e7f5e1;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        color: #1a1a1a;
    }}
    .stButton > button {{
        background-color: #2196f3;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }}
    .stButton > button:hover {{
        background-color: #1976d2;
    }}
</style>
""", unsafe_allow_html=True)

# Streamlit UI Setup
st.title("♻️ Waste Classification System")
st.markdown("<p class='header-title'>Upload an image of waste to classify and receive recycling or reusing suggestions!</p>", unsafe_allow_html=True)

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="file_uploader_1")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("🔍 Analyzing the image...")

    # Preprocess the image
    image_data = preprocess_image(image)

    # Make prediction
    prediction = model.predict(image_data)
    index = np.argmax(prediction)
    confidence_score = prediction[0][index]

    # Display the result
    predicted_label = class_names[index] if index < len(class_names) else "Unknown"
    st.success(f"🗑️ Predicted Waste Type: **{predicted_label}**")
    st.write(f"Confidence Score: {confidence_score * 100:.2f}%")

    # Provide suggestions based on predicted label
    provide_suggestions(predicted_label)

# Function to provide suggestions
def provide_suggestions(predicted_label):
    suggestions = {
        "Cardboard": {
            "steps": [
                "1. **Flatten** the cardboard.",
                "2. **Remove** any non-recyclable components (like plastic windows).",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/cardboard.jpg"  # Replace with a valid image URL
        },
        "Compost": {
            "steps": [
                "1. **Collect** kitchen scraps and yard waste.",
                "2. **Add** to a compost bin.",
                "3. **Turn** regularly to aerate and speed up decomposition."
            ],
            "image": "https://example.com/compost.jpg"
        },
        # Add similar entries for other classes
    }

    if predicted_label in suggestions:
        st.subheader("🔄 Suggestions for Recycling/Reusing/Degrading:")
        for step in suggestions[predicted_label]["steps"]:
            st.markdown(f"<div class='step'>{step}</div>", unsafe_allow_html=True)
        st.image(suggestions[predicted_label]["image"], caption=f"How to handle {predicted_label}", use_column_width=True)
    else:
        st.warning("No specific suggestions found for this type of waste.")
