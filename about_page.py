import streamlit as st

def show_about_page():
    st.title("About This App")
    st.markdown("""
    Welcome to the Intelligent Waste Classification App! This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
    """)

    # Mission Section
    st.subheader("Our Mission")
    st.markdown("""
    Our mission is to encourage sustainable waste management practices by providing an easy-to-use tool that educates and empowers users to make better recycling choices.
    """)

    # Team Section
    st.subheader("Meet the Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://example.com/vidhi.jpg", caption="Vidhi Dhakate", use_column_width=True)
        st.markdown("**Vidhi Dhakate**\nLead Developer")

    with col2:
        st.image("https://example.com/kashish.jpg", caption="Kashish Pawar", use_column_width=True)
        st.markdown("**Kashish Pawar**\nData Scientist")

    with col3:
        st.image("https://example.com/tejas.jpg", caption="Tejas Mahakalkar", use_column_width=True)
        st.markdown("**Tejas Mahakalkar**\nProject Manager")

    # Future Work Section
    st.subheader("Future Work")
    st.markdown("""
    - **Real-Time Feedback:** Allow users to receive instant feedback on their recycling practices.
    - **Expand Waste Categories:** Continue adding more waste categories for better identification.
    - **Community Features:** Enable users to share recycling tips and challenges.
    """)
