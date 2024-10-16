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
    .dark-theme {
        background-color: #333;
        color: #fff;
    }
    .light-theme {
        background-color: #f7f9fc;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for theme management
if 'dark_theme' not in st.session_state:
    st.session_state.dark_theme = False

# Theme toggle function
def toggle_theme():
    st.session_state.dark_theme = not st.session_state.dark_theme

# Main function to navigate through the pages
def main():
    # Set the theme based on user preference
    if st.session_state.dark_theme:
        st.markdown('<style>body { background-color: #333; color: #fff; }</style>', unsafe_allow_html=True)
    else:
        st.markdown('<style>body { background-color: #f7f9fc; color: #000; }</style>', unsafe_allow_html=True)

    # Sidebar for navigation
    st.sidebar.title("Navigation")

    # Theme toggle button
    theme_button = st.sidebar.button("🌙 Toggle Dark/Light Theme", on_click=toggle_theme)

    # Search bar for quick navigation
    search_term = st.sidebar.text_input("Search...", placeholder="Type to search...")

    # Create a section for page navigation
    st.sidebar.markdown("### Pages")
    
    # Buttons for navigation with tooltips
    home_button = st.sidebar.button("🏠 Home", key="home")
    classification_button = st.sidebar.button("🔍 Classification", key="classification")
    about_button = st.sidebar.button("ℹ️ About", key="about")
    
    # Track the current page and implement transitions
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
        # User profile/settings button
        st.sidebar.button("👤 Profile")
        st.sidebar.button("⚙️ Settings")
        st.sidebar.button("❓ Help")

    # Display progress indicator or breadcrumb
    st.sidebar.markdown("### Current Page: " + ("Home" if home_button else "Classification" if classification_button else "About"))

if __name__ == "__main__":
    main()
