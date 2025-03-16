import streamlit as st

def show_contact_page():
    
    st.title("Contact Us")
    
    st.markdown("""
    If you have any questions, suggestions, or feedback, feel free to reach out to us!

    - **Vidhi Dhakate**: 
      - Email: dhakatevs@rknec.edu
      - Mobile: +91 982329xxxx

      <br>

    - **Tejas Mahakalkar**: 
      - Email: mahakalkarth@rknec.edu
      - Mobile: +91 755913xxxx

      <br>

    - **Kashish Pawar**: 
      - Email: pawarkn@rknec.edu
      - Mobile: +91 704922xxxx
    """, unsafe_allow_html=True)
