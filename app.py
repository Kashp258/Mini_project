import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained model
model = load_model('waste_classifications_model.keras')

# Define the categories
categories = ['cardboard', 'compost', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Function to preprocess the image for the model
def preprocess_image(image):
    image = cv2.resize(image, (224, 224))  # Resize the image to 224x224
    image = image.astype('float32') / 255.0  # Normalize the image
    image = img_to_array(image)  # Convert to array
    image = np.expand_dims(image, axis=0)  # Expand dimensions
    return image

# Create a title for the app
st.title("Waste Classification Using Deep Learning")

# Set up the webcam
st.write("Webcam feed:")
run = st.checkbox('Run Webcam')
FRAME_WINDOW = st.image([])

# Capture video from the webcam
cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the captured frame
    FRAME_WINDOW.image(frame)

    # Process the frame when the user clicks a button
    if st.button("Classify"):
        # Preprocess the image
        processed_image = preprocess_image(frame)

        # Make predictions
        predictions = model.predict(processed_image)
        predicted_class = categories[np.argmax(predictions)]
        confidence = np.max(predictions)

        # Show the results
        st.write(f"Predicted class: {predicted_class} with confidence {confidence:.2f}")

cap.release()
