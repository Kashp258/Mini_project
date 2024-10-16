import streamlit as st
from home_page import show_home_page
from classification_page import show_classification_page
from about_page import show_about_page

# Main function to navigate through the pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Classification", "About"))

    if page == "Home":
        show_home_page()
    elif page == "Classification":
        show_classification_page()
    elif page == "About":
        show_about_page()

if __name__ == "__main__":
    main()
