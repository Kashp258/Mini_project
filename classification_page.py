import streamlit as st
import numpy as np
import os
from PIL import Image
from utils import preprocess, model_arc, gen_labels
import gdown

# Background image URL
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"

# Function to download the model from Google Drive
def download_model_from_drive():
    file_id = '1ruV_1zQcxd4E2-5c0dhIK3vQhlWNMQRb'  # Your Google Drive file ID
    url = f'https://drive.google.com/uc?id={file_id}'
    output = './weights/weights/modeltrash.weights.h5'  # Path to save the downloaded file

    # Check if the model weights are already downloaded
    if not os.path.exists(output):
        st.write("Downloading model weights from Google Drive...")
        os.makedirs('./weights', exist_ok=True)  # Ensure the weights folder exists
        gdown.download(url, output, quiet=False)
    else:
        st.write("Model weights already downloaded.")

# Path to the downloaded model weights
model_weights_path = './weights/weights/modeltrash.weights.h5'

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_model():
    model = model_arc()  # Get the architecture from utils.py
    if os.path.exists(model_weights_path):
        st.write("Model weights found, loading...")
        model.load_weights(model_weights_path)  # Load saved weights
    else:
        st.error("Model weights file not found. Please check the path.")
    return model

def show_classification_page():
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
            color: #1a1a1a;  /* Darker font color for improved contrast */
            font-size: 28px;
            font-weight: bold;
        }}
        p, ul {{
            color: #1a1a1a;  /* Standard text color */
        }}
        .step {{
            background-color: #e7f5e1;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            color: #1a1a1a;  /* Ensure text is visible */
        }}
        .stButton > button {{
            background-color: #2196f3;  /* Bright blue button */
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }}
        .stButton > button:hover {{
            background-color: #1976d2;  /* Darker blue on hover */
        }}
    </style>
    """, unsafe_allow_html=True)

    # Advanced user interface setup
    st.title("♻️ Waste Classification System")
    
    st.markdown("<p class='header-title'>Upload an image of waste to classify and receive recycling or reusing suggestions!</p>", unsafe_allow_html=True)

    # File uploader widget for image input
    image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="file_uploader_1")

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("🔍 Analyzing the image...")

        # Preprocess the uploaded image
        try:
            image_array = preprocess(image)
        except Exception as e:
            st.error(f"Error in preprocessing the image: {e}")
            return

        # Load the model
        model = load_model()

        # Predict using the loaded model
        try:
            prediction = model.predict(image_array)
            # Get the predicted class index and label
            predicted_class = np.argmax(prediction, axis=1)

            # Get class labels
            labels = gen_labels()
            predicted_label = labels[predicted_class[0]] if predicted_class[0] < len(labels) else "Unknown"

            # Display the prediction
            st.success(f"🗑️ Predicted Waste Type: **{predicted_label}**")

            # Suggestions based on predicted label
            provide_suggestions(predicted_label)
        except Exception as e:
            st.error(f"Error during prediction: {e}")

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
            "image": "https://example.com/compost.jpg"  # Replace with a valid image URL
        },
        "Glass": {
            "steps": [
                "1. **Rinse** the glass container.",
                "2. **Remove** any lids or caps.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/glass.jpg"  # Replace with a valid image URL
        },
        "Metal": {
            "steps": [
                "1. **Clean** the metal item to remove food residue.",
                "2. **Check** for any specific recycling instructions.",
                "3. **Place** in the metal recycling bin."
            ],
            "image": "https://example.com/metal.jpg"  # Replace with a valid image URL
        },
        "Paper": {
            "steps": [
                "1. **Remove** any staples or paperclips.",
                "2. **Flatten** and sort the paper.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/paper.jpg"  # Replace with a valid image URL
        },
        "Plastic": {
            "steps": [
                "1. **Rinse** the plastic container.",
                "2. **Check** the recycling symbol for instructions.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/plastic.jpg"  # Replace with a valid image URL
        }
    }

    if predicted_label in suggestions:
        st.subheader("🔄 Suggestions for Recycling/Reusing/Degrading:")
        for step in suggestions[predicted_label]["steps"]:
            st.markdown(f"<div class='step'>{step}</div>", unsafe_allow_html=True)
        st.image(suggestions[predicted_label]["image"], caption=f"How to handle {predicted_label}", use_column_width=True)

    else:
        st.warning("No specific suggestions found for this type of waste.")
