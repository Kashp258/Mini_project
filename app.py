import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page

# Custom CSS for the sidebar
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f7f9fc;  /* Light background */
        border-radius: 8px;
        padding: 10px;
    }
    .btn {
        display: inline-block;
        padding: 10px 20px;
        margin: 5px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        color: white;
        background-color: #2196f3;  /* Primary button color */
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .btn:hover {
        background-color: #1976d2;  /* Darker blue on hover */
    }
    .active {
        background-color: #1976d2;  /* Active button color */
    }
    </style>
""", unsafe_allow_html=True)

# Main function to navigate through the pages
def main():
    # Set up the sidebar for navigation
    st.sidebar.title("Navigation")
    
    # Create a section for page navigation
    st.sidebar.markdown("### Pages")
    
    # Buttons for navigation with tooltips
    home_button = st.sidebar.button("🏠 Home", key="home")
    classification_button = st.sidebar.button("🔍 Classification", key="classification")
    about_button = st.sidebar.button("ℹ️ About", key="about")
    
    # Track the current page
    if home_button:
        show_home_page()
    elif classification_button:
        show_classification_page()
    elif about_button:
        show_about_page()

    # Highlight the active button
    if home_button:
        st.sidebar.markdown("<div class='active'>Home</div>", unsafe_allow_html=True)
    elif classification_button:
        st.sidebar.markdown("<div class='active'>Classification</div>", unsafe_allow_html=True)
    elif about_button:
        st.sidebar.markdown("<div class='active'>About</div>", unsafe_allow_html=True)

    # Expandable section for additional options
    with st.sidebar.expander("More Options", expanded=False):
        st.sidebar.markdown("You can explore other features and settings here.")
        # Add additional buttons or links as needed
        st.sidebar.button("Settings")
        st.sidebar.button("Help")

if __name__ == "__main__":
    main()
