import streamlit as st

def show_about_page():
    st.title("About This App")
    st.write("""
        This app uses machine learning to classify different types of waste 
        and provides recommendations for recycling or disposal. It is part of 
        an initiative to promote better waste management practices.
    """)
