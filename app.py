import streamlit as st

# Navigation function to render the navigation bar
def navigation():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    
    # Create navigation options
    options = ["Home", "Classification", "About", "Contact"]
    
    # Add radio buttons for navigation
    selected_option = st.sidebar.radio("Select a page:", options)

    return selected_option

def main():
    # Call the navigation function
    selected_page = navigation()
    
    if selected_page == "Home":
        show_home_page()
    elif selected_page == "Classification":
        show_classification_page()
    elif selected_page == "About":
        show_about_page()
    elif selected_page == "Contact":
        show_contact_page()

# Function to display the About page
def show_about_page():
    st.title("About This Application")
    st.markdown("""
    This Intelligent Waste Classification App aims to simplify waste management 
    through advanced machine learning models. By classifying waste into various 
    categories, it provides users with insights on how to dispose of, recycle, or reuse waste 
    materials effectively.
    """)
    st.image("https://example.com/about-image.jpg", use_column_width=True)  # Replace with a valid image URL

# Function to display the Contact page
def show_contact_page():
    st.title("Contact Us")
    st.markdown("""
    For any inquiries or feedback, please reach out to us at:
    
    - Email: support@example.com
    - Phone: +1-234-567-890
    """)
    st.image("https://example.com/contact-image.jpg", use_column_width=True)  # Replace with a valid image URL

if __name__ == "__main__":
    main()
