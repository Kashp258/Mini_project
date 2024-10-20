import streamlit as st
from PIL import Image
import base64
from classification_page import show_classification_page
from about_page import show_about_page

# Load the background image
def get_base64_of_img(img):
    with open(img, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Background image path
background_image_path = "green_bg_image.png"
background_image_base64 = get_base64_of_img(background_image_path)

def show_home_page():
    # Custom CSS for better aesthetics and background image
    st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{background_image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
            color: #1a1a1a;
        }}
        .header-title {{
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-top: 50px;
            text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.9);
            animation: fadeIn 1s;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        .intro {{
            font-size: 22px;
            text-align: center;
            margin: 20px auto;
            max-width: 800px;
            animation: slideIn 1s;
        }}
        @keyframes slideIn {{
            from {{ transform: translateY(-20px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}
        .feature {{
            background-color: rgba(255, 255, 255, 0.9); /* Slightly transparent background */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }}
        .feature:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 30px rgba(0, 0, 0, 0.25);
        }}
        .feature-title {{
            font-weight: bold;
            color: #2196f3;
            font-size: 24px;
            margin-bottom: 10px;
        }}
        .stButton > button {{
            background-color: #4caf50;  /* Green button */
            color: white;
            padding: 12px 24px;
            font-size: 18px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
        }}
        .stButton > button:hover {{
            background-color: #388e3c;  /* Darker green on hover */
            transform: scale(1.05);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25);
        }}
        footer {{
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #555;
        }}
        .stats-container {{
            text-align: center;
            margin: 40px 0;
            animation: bounceIn 1s;
        }}
        @keyframes bounceIn {{
            0% {{ transform: scale(0); }}
            50% {{ transform: scale(1.1); }}
            100% {{ transform: scale(1); }}
        }}
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='header-title'>Welcome to the Intelligent Waste Classification App!</h1>", unsafe_allow_html=True)
    
    # Introduction Section
    st.markdown("<p class='intro'>**This application helps you classify waste into different categories effortlessly.**</p>", unsafe_allow_html=True)
    st.markdown("<p class='intro'>Whether you are at home, at school, or in a business, understanding how to manage your waste is critical for a cleaner and greener environment.</p>", unsafe_allow_html=True)

    # Features Section
    st.subheader("Why Use This Application?")
    
    feature_list = [
        ("Accurate Classification", "Utilizes state-of-the-art machine learning models to accurately classify various waste types."),
        ("Real-Time Suggestions", "Receive instant suggestions on recycling, reusing, or disposing of waste responsibly."),
        ("Easy to Use", "Simply upload an image, and the app intelligently categorizes your waste."),
        ("Educational Resources", "Learn about waste management and how you can contribute to a sustainable future.")
    ]

    for title, description in feature_list:
        st.markdown(f"<div class='feature' onclick=\"alert('Feature: {title}')\"><div class='feature-title'>{title}</div><p>{description}</p></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<footer>Powered by Streamlit & Machine Learning</footer>", unsafe_allow_html=True)

# Call the function to show the home page
if __name__ == "__main__":
    show_home_page()
