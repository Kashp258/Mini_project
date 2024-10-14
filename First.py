import streamlit as st
import numpy as np
import os
from PIL import Image
from utils import preprocess, model_arc, gen_labels
import gdown  # Importing gdown to download from Google Drive

# Function to download the model from Google Drive
def download_model_from_drive():
    file_id = '1ruV_1zQcxd4E2-5c0dhIK3vQhlWNMQRb'  # Your correct Google Drive file ID
    url = f'https://drive.google.com/uc?id={file_id}'
    output = './weights/modeltrash.weights.h5'  # Path to save the downloaded file

    # Check if the model weights are already downloaded, if not, download them
    if not os.path.exists(output):
        st.write("Downloading model weights from Google Drive...")
        os.makedirs('./weights', exist_ok=True)  # Ensure the weights folder exists
        gdown.download(url, output, quiet=False)
    else:
        st.write("Model weights already downloaded.")

# Download the model if not present
download_model_from_drive()

# Path to the downloaded model weights
model_weights_path = './weights/modelnew.weights.h5'

# Cache the model loading to avoid reloading on every interaction
@st.cache_resource
def load_model():
    model = model_arc()  # Get the architecture from utils.py
    if os.path.exists(model_weights_path):
        model.load_weights(model_weights_path)  # Load saved weights
    else:
        st.error("Model weights file not found. Please check the path.")
    return model

# Load the model when the app starts
model = load_model()

# Function to provide detailed, step-wise suggestions with images
def get_detailed_suggestions(class_name):
    suggestions = {
        "Cardboard": {
            "steps": [
                "Step 1: Flatten the cardboard boxes.",
                "Step 2: Remove any plastic tape or labels.",
                "Step 3: Take the flattened cardboard to a recycling facility or drop it in the appropriate recycling bin."
            ],
            "image_urls": [
                "https://example.com/flatten-cardboard.jpg",
                "https://example.com/remove-tape.jpg",
                "https://example.com/recycling-bin.jpg"
            ]
        },
        "Compost": {
            "steps": [
                "Step 1: Collect compostable waste like food scraps and yard waste.",
                "Step 2: Chop waste into smaller pieces for faster decomposition.",
                "Step 3: Layer green (nitrogen-rich) and brown (carbon-rich) materials.",
                "Step 4: Turn the pile regularly to aerate it and speed up composting."
            ],
            "image_urls": [
                "https://example.com/collect-waste.jpg",
                "https://example.com/chop-waste.jpg",
                "https://example.com/layer-materials.jpg",
                "https://example.com/turn-pile.jpg"
            ]
        },
        # Add similar entries for "Glass", "Metal", "Paper", "Plastic"
        # Include images to explain each step clearly
    "Glass": {
            "steps": [
                "Step 1: Rinse the glass items to remove any leftover contents.",
                "Step 2: Separate glass by color (clear, green, brown) if required by your local recycling facility.",
                "Step 3: Take the clean, sorted glass to a recycling drop-off point or place it in the recycling bin."
            ],
            "image_urls": [
                "https://example.com/rinse-glass.jpg",
                "https://example.com/sort-glass.jpg",
                "https://example.com/recycle-glass.jpg"
            ]
        },
        "Metal": {
            "steps": [
                "Step 1: Rinse metal cans or containers to remove food or liquid residue.",
                "Step 2: Crush cans to save space in your recycling bin.",
                "Step 3: Take the metal items to a recycling facility or leave them in the appropriate curbside bin."
            ],
            "image_urls": [
                "https://example.com/rinse-metal.jpg",
                "https://example.com/crush-cans.jpg",
                "https://example.com/recycle-metal.jpg"
            ]
        },
        "Paper": {
            "steps": [
                "Step 1: Sort paper into categories: newspaper, office paper, cardboard, etc.",
                "Step 2: Remove any staples, tape, or plastic coverings.",
                "Step 3: Place sorted paper in the recycling bin or drop it at a recycling center."
            ],
            "image_urls": [
                "https://example.com/sort-paper.jpg",
                "https://example.com/remove-staples.jpg",
                "https://example.com/recycle-paper.jpg"
            ]
        },
        "Plastic": {
            "steps": [
                "Step 1: Check the recycling number on the plastic item to ensure it is recyclable in your area.",
                "Step 2: Rinse and clean the plastic containers to remove any food or drink residue.",
                "Step 3: Crush plastic bottles and containers to save space.",
                "Step 4: Take clean, sorted plastic to a recycling facility or place it in the correct recycling bin."
            ],
            "image_urls": [
                "https://example.com/check-recycle-number.jpg",
                "https://example.com/rinse-plastic.jpg",
                "https://example.com/crush-plastic.jpg",
                "https://example.com/recycle-plastic.jpg"
            ]
        }
    }
    return suggestions.get(class_name, {"steps": ["No specific suggestions available."], "image_urls": []})

# Define background and UI
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Waste Classification Model")
st.write("Upload an image of waste for classification.")

# File uploader widget for image input
image_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], key="file_uploader_1")

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    st.write("Classifying...")

    # Preprocess the uploaded image
    image_array = preprocess(image)

    # Predict using the loaded model
    prediction = model.predict(image_array)

    # Get the predicted class index and label
    predicted_class = np.argmax(prediction, axis=1)
    
    # Get class labels (you need to define these in utils.py)
    labels = gen_labels()
    predicted_label = labels[predicted_class[0]]

    # Display the prediction
    st.write(f"Predicted Class: {predicted_label}")

    # Display detailed suggestions with images
    suggestions = get_detailed_suggestions(predicted_label)
    st.write("Step-by-Step Suggestions:")
    for step, img_url in zip(suggestions["steps"], suggestions["image_urls"]):
        st.write(step)
        if img_url:
            st.image(img_url, use_column_width=True)
