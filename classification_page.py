import streamlit as st
import numpy as np
import os
from PIL import Image, ImageOps
from keras.models import load_model

# Background image URL
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"

# Function to load the model
@st.cache_resource
def load_trained_model():
    try:
        model = load_model("keras_model.h5", compile=False)
        st.write("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to preprocess the image
def preprocess_image(image):
    # Convert image to RGB and resize
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    # Turn image into numpy array and normalize
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # Expand dimensions to match input shape for model
    data = np.expand_dims(normalized_image_array, axis=0)
    return data

# Function to display suggestions
def provide_suggestions(predicted_label):
    suggestions = {
        "Cardboard": {
            "steps": [
                "1. **Flatten** the cardboard.",
                "2. **Remove** any non-recyclable components (like plastic windows).",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/cardboard.jpg"
        },
        "Compost": {
            "steps": [
                "1. **Collect** kitchen scraps and yard waste.",
                "2. **Add** to a compost bin.",
                "3. **Turn** regularly to aerate and speed up decomposition."
            ],
            "image": "https://example.com/compost.jpg"
        },
        "Glass": {
            "steps": [
                "1. **Rinse** the glass container.",
                "2. **Remove** any lids or caps.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/glass.jpg"
        },
        "Metal": {
            "steps": [
                "1. **Clean** the metal item to remove food residue.",
                "2. **Check** for any specific recycling instructions.",
                "3. **Place** in the metal recycling bin."
            ],
            "image": "https://example.com/metal.jpg"
        },
        "Paper": {
            "steps": [
                "1. **Remove** any staples or paperclips.",
                "2. **Flatten** and sort the paper.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/paper.jpg"
        },
        "Plastic": {
            "steps": [
                "1. **Rinse** the plastic container.",
                "2. **Check** the recycling symbol for instructions.",
                "3. **Place** in the recycling bin."
            ],
            "image": "https://example.com/plastic.jpg"
        }
    }
    if predicted_label in suggestions:
        st.subheader("🔄 Suggestions for Recycling/Reusing/Degrading:")
        for step in suggestions[predicted_label]["steps"]:
            st.markdown(f"<div class='step'>{step}</div>", unsafe_allow_html=True)
        st.image(suggestions[predicted_label]["image"], caption=f"How to handle {predicted_label}", use_column_width=True)
    else:
        st.warning("No specific suggestions found for this type of waste.")

# Main function to run the Streamlit app
def main():
    # Custom CSS for background image
    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
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
        }}
        .stButton > button:hover {{
            background-color: #1976d2;
        }}
    </style>
    """, unsafe_allow_html=True)

    # App title and instructions
    st.title("♻️ Waste Classification System")
    st.markdown("<p class='header-title'>Upload an image of waste to classify and receive recycling or reusing suggestions!</p>", unsafe_allow_html=True)

    # File uploader
    image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        image = Image.open(image_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("🔍 Analyzing the image...")

        # Preprocess image
        data = preprocess_image(image)

        # Load the model
        model = load_trained_model()

        if model:
            try:
                # Predict using the model
                prediction = model.predict(data)
                index = np.argmax(prediction)
                
                # Load labels
                with open("labels.txt", "r") as file:
                    labels = [line.strip() for line in file.readlines()]
                
                # Get the predicted label
                predicted_label = labels[index]
                st.success(f"🗑️ Predicted Waste Type: **{predicted_label}**")

                # Provide suggestions
                provide_suggestions(predicted_label)

            except Exception as e:
                st.error(f"Error during prediction: {e}")

if __name__ == "__main__":
    main()
