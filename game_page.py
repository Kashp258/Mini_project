# game_page.py

import streamlit as st

# Function to show the gamification page
def show_gamification_page():
    # Initialize session state for points and badges
    if 'points' not in st.session_state:
        st.session_state.points = 0
    if 'badges' not in st.session_state:
        st.session_state.badges = []

    st.title("Gamification Feature 🎮")
    st.write("Welcome to the Gamification Page! Earn points and badges by classifying waste.")

    # Display points
    st.write(f"**Points:** {st.session_state.points}")
    
    # Display badges
    st.write("**Badges Earned:**")
    if st.session_state.badges:
        for badge in st.session_state.badges:
            st.markdown(f"- {badge}")
    else:
        st.write("No badges earned yet.")

    # Sample challenge
    st.write("### Challenges")
    if st.button("Complete a Challenge!"):
        challenge_points = 10  # Points for completing a challenge
        st.session_state.points += challenge_points
        st.session_state.badges.append("Challenge Champion!")
        st.success(f"You earned {challenge_points} points! 🎉")

