import streamlit as st

def show_home_page():
    # Custom CSS for better aesthetics
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f5f5f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .header {
            text-align: center;
            padding: 50px 0;
            color: #2c3e50;
        }
        .btn-primary {
            background-color: #3498db;
            color: white;
            padding: 15px 30px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 18px;
        }
        .btn-primary:hover {
            background-color: #2980b9;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

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
