import streamlit as st
import os
import numpy as np
from keras.models import load_model
from keras.layers import DepthwiseConv2D
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input

# Background image URL
background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"

# Apply custom CSS to add the background image and improve layout
page_bg_css = f"""
<style>
    body {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-attachment: fixed;
        color: #222;
        font-family: 'Arial', sans-serif;
    }}
    .main {{
        background: rgba(255, 255, 255, 0.85); /* Slightly transparent background for content */
        border-radius: 15px;
        padding: 20px;
    }}
    h1, h2, h3, p {{
        color: #333;
    }}
    .sidebar .sidebar-content {{
        background: rgba(50, 115, 50, 0.9); /* Darker green for sidebar */
        color: white;
    }}
    .stButton > button {{
        color: white;
        background-color: #4CAF50;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: #3e8e41;
    }}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

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

# Function to load labels
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

# Real-time suggestions based on waste type
def get_recycling_tips(waste_type):
    tips = {
        "cardboard": "📦 **Recycle Tips:** Break down the boxes and keep them dry. Recycle at your local center. **Reuse:** Consider using it for storage or craft projects.",
        "compost": "🍂 **Compost Tips:** Add to your compost bin. Great for enriching soil. **Reduce:** Use kitchen waste efficiently, freeze for future use.",
        "glass": "🍾 **Recycle Tips:** Rinse and separate by color if required. **Reuse:** Use jars for storage or DIY crafts. **Note:** Avoid mixing with other waste!",
        "metal": "🛠️ **Recycle Tips:** Separate ferrous (magnetic) and non-ferrous metals. **Reuse:** Donate or sell scrap metal. **Warning:** Handle sharp metal carefully!",
        "paper": "📄 **Recycle Tips:** Keep dry and clean. **Reuse:** Use for notes, crafts, or as wrapping paper. **Tip:** Consider going paperless whenever possible!",
        "plastic": "♻️ **Recycle Tips:** Check the recycling symbol. **Reuse:** Use durable plastics for multiple purposes. **Avoid:** Single-use plastics whenever possible."
    }
    return tips.get(waste_type.lower(), "❓ **General Tip:** Always check local guidelines to see how you can properly recycle or dispose of this type of waste.")

# Fun facts to keep users engaged
def get_fun_fact():
    facts = [
        "🌍 Did you know? Recycling a single aluminum can saves enough energy to run a TV for three hours!",
        "♻️ Plastic can take up to 500 years to decompose in a landfill. Reduce, Reuse, Recycle!",
        "🌿 Composting helps reduce greenhouse gases. Food scraps can become nutrient-rich soil instead of harmful methane.",
        "📦 Every ton of recycled paper saves 17 trees! Small efforts can make a big difference."
    ]
    return np.random.choice(facts)

# Show classification page
def show_classification_page():
    st.title("🌱 Waste Classification App")
    st.markdown("### 🌟 Upload an image of waste to identify its type and get helpful tips for proper recycling. 🌎 Together, we can make a difference!")
    st.sidebar.title("Quick Tips 💡")
    st.sidebar.info(get_fun_fact())

    # Load the model and labels
    try:
        model = load_model_func()
        labels = load_labels()
        st.success("✅ Model and labels loaded successfully!")
    except Exception as e:
        st.error(f"❌ Error loading model or labels: {e}")
        return

    # Image upload
    uploaded_file = st.file_uploader("📷 Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        st.write("🖼️ **Image uploaded successfully!**")
        
        if model is not None and labels is not None:
            image_data = preprocess_image(uploaded_file)
            predictions = model.predict(image_data)
            predicted_label = labels[np.argmax(predictions)]
            
            # Display the predicted label
            st.write(f"🗑️ **Predicted Label:** {predicted_label}")
            
            # Show real-time suggestions based on the classification
            suggestions = get_recycling_tips(predicted_label)
            st.info(f"💡 **Recycling Tip:** {suggestions}")
        else:
            st.error("⚠️ Model or labels not available. Please check if they were loaded correctly.")
