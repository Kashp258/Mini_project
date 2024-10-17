import streamlit as st

def show_about_page():
    # Apply background image style
    background_image_url = "https://png.pngtree.com/thumb_back/fh260/background/20220217/pngtree-green-simple-atmospheric-waste-classification-illustration-background-image_953325.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({background_image_url});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page content
    st.title("About This App")
    st.markdown("""
    Welcome to the **Intelligent Waste Classification App**! 🌍 This tool utilizes cutting-edge machine learning to help users identify different types of waste and offers useful suggestions on recycling, reusing, and proper disposal.
    """)

    # Mission Section
    st.subheader("Our Mission 🎯")
    st.markdown("""
    Our mission is to encourage sustainable waste management practices by providing an easy-to-use tool that educates and empowers users to make better recycling choices. We believe that small actions can lead to significant environmental changes.
    """)

    # Team Section
    st.subheader("Meet the Team 👥")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://www.google.com/imgres?q=wolverine%20images&imgurl=https%3A%2F%2Fcomicbook.com%2Fwp-content%2Fuploads%2Fsites%2F4%2F2024%2F08%2F1896ecc8-3e07-42b6-9162-c8e392ff8c1e.jpg&imgrefurl=https%3A%2F%2Fcomicbook.com%2Fmovies%2Fnews%2Fdeadpool-wolverine-hugh-jackman-wolverine-suit-full-reveal-mcu%2F&docid=a6x313Zj8ZqagM&tbnid=6IX_PKbJYJrQ6M&vet=12ahUKEwjCzIHbgJaJAxUlr1YBHY9WLAgQM3oECEYQAA..i&w=1200&h=675&hcb=2&ved=2ahUKEwjCzIHbgJaJAxUlr1YBHY9WLAgQM3oECEYQAA", caption="Vidhi Dhakate", use_column_width=True)
        st.markdown("**Vidhi Dhakate**\nLead Developer")

    with col2:
         st.image("https://www.google.com/imgres?q=dogpool%20images&imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fmarvelcinematicuniverse%2Fimages%2Ff%2Ff0%2FDogpool.png%2Frevision%2Flatest%3Fcb%3D20240628012200&imgrefurl=https%3A%2F%2Fmarvelcinematicuniverse.fandom.com%2Fwiki%2FDogpool&docid=0ADLUB9ofx56JM&tbnid=Idtkl3VyN6QGmM&vet=12ahUKEwihrYTvgJaJAxVgk1YBHX4BHgAQM3oECGUQAA..i&w=1080&h=1080&hcb=2&ved=2ahUKEwihrYTvgJaJAxVgk1YBHX4BHgAQM3oECGUQAA", caption="Tejas Mahakalkar", use_column_width=True)
         st.markdown("**Tejas Mahakalkar**\nProject Manager")

    with col3:
        st.image("https://www.google.com/imgres?q=deadpool%20images&imgurl=https%3A%2F%2Fhips.hearstapps.com%2Fhmg-prod%2Fimages%2Fdeadpool-and-wolverine-trailer-6626623ab898e.jpg%3Fcrop%3D0.410xw%3A1.00xh%3B0.221xw%2C0%26resize%3D1200%3A*&imgrefurl=https%3A%2F%2Fwww.digitalspy.com%2Fmovies%2Fa862002%2Fdeadpool-3-release-date-cast-plot-trailer-ryan-reynolds%2F&docid=4DOIk_SOb-TyyM&tbnid=iCGEjbfKQTr7XM&vet=12ahUKEwjVgK2LgJaJAxVz2jQHHegvPdgQM3oECBcQAA..i&w=787&h=784&hcb=2&ved=2ahUKEwjVgK2LgJaJAxVz2jQHHegvPdgQM3oECBcQAA", caption="Kashish Pawar", use_column_width=True)
        st.markdown("**Kashish Pawar**\nData Scientist")

    # Future Work Section
    st.subheader("Future Work 🚀")
    st.markdown("""
    - **Real-Time Feedback:** Allow users to receive instant feedback on their recycling practices.
    - **Expand Waste Categories:** Continue adding more waste categories for better identification.
    - **Community Features:** Enable users to share recycling tips and challenges.
    - **Gamification Elements:** Introduce badges and rewards for active participants to encourage engagement.
    - **Educational Resources:** Provide articles and resources on sustainability practices to enhance user knowledge.
    """)

    # Call to Action Section
    st.subheader("Get Involved! 🤝")
    st.markdown("""
    Join us in our mission to create a cleaner, greener planet! Here are some ways you can contribute:
    - **Spread the Word:** Share this app with friends and family to raise awareness about waste management.
    - **Participate in Local Clean-Up Events:** Get involved in your community and help keep your environment clean.
    - **Follow Us on Social Media:** Stay updated on our latest features and sustainability tips.
    """)

    st.success("Thank you for supporting sustainable practices! Together, we can make a difference!")
