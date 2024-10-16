import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page

# Main function to navigate through the pages
def main():
    # Set up the sidebar for navigation
    st.sidebar.title("Navigation")
    
    # Create radio buttons for navigation with icons
    page = st.sidebar.radio(
        "Go to:",
        ("🏠 Home", "🔍 Classification", "ℹ️ About"),
        index=0,  # Default selected page
        label_visibility="collapsed"  # Hide the label for a cleaner look
    )

    # Add descriptions for better user guidance
    st.sidebar.markdown(
        """
        Navigate through the application using the options above.
        - **Home:** Introduction to the Intelligent Waste Classification App.
        - **Classification:** Upload an image and classify your waste.
        - **About:** Learn more about the app and its development.
        """
    )

    # Call the corresponding page function based on the selected option
    if page == "🏠 Home":
        show_home_page()
    elif page == "🔍 Classification":
        show_classification_page()
    elif page == "ℹ️ About":
        show_about_page()

if __name__ == "__main__":
    main()
