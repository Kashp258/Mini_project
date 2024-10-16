import streamlit as st

def show_home_page():
    # Custom CSS for better aesthetics
 st.markdown("""
<style>
    .stApp {
        background-color: #f7f9fc;  /* Light background */
        font-family: 'Arial', sans-serif;
    }
    .header-title {
        color: #1a1a1a;  /* Darker font color for improved contrast */
        font-size: 28px;
        font-weight: bold;
    }
    p, ul {
        color: #1a1a1a;  /* Standard text color */
    }
    .step {
        background-color: #e7f5e1;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        color: #1a1a1a;  /* Ensure text is visible */
    }
    .stButton > button {
        background-color: #2196f3;  /* Bright blue button */
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #1976d2;  /* Darker blue on hover */
    }
</style>
""", unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='header'>Welcome to the Intelligent Waste Classification App!</h1>", unsafe_allow_html=True)
    
    # Add Hero Image
    st.image("https://example.com/hero-image.jpg", use_column_width=True)
    
    # Introduction Section
    st.markdown("""
    **This application helps you classify waste into different categories effortlessly.**
    Whether you are at home, at school, or in a business, understanding how to manage your waste is critical for a cleaner and greener environment. 
    """)

    # Call to Action Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            "<a href='#' class='btn-primary' onclick='window.location.href = \"/?Classification\";'>Get Started</a>",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<a href='#' class='btn-primary' onclick='window.location.href = \"/?About\";'>Learn More</a>",
            unsafe_allow_html=True
        )

    # Features Section
    st.subheader("Why Use This Application?")
    st.markdown("""
    - **Accurate Classification:** Utilizes state-of-the-art machine learning models.
    - **Real-Time Suggestions:** Receive suggestions on recycling, reusing, or disposing of waste.
    - **Easy to Use:** Simply upload an image, and the app does the rest.
    - **Educational:** Helps users understand how to manage waste efficiently.
    """)

    # Footer
    st.markdown("<footer style='text-align: center; padding-top: 20px;'>Powered by Streamlit & Machine Learning</footer>", unsafe_allow_html=True)
