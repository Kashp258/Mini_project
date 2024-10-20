# game_page.py

import streamlit as st
import random

# Function to show the gamification page
def show_gamification_page():
    # Initialize session state for points and badges
    if 'points' not in st.session_state:
        st.session_state.points = 0
    if 'badges' not in st.session_state:
        st.session_state.badges = []
    if 'leaderboard' not in st.session_state:
        st.session_state.leaderboard = {}

    st.title("Gamification Feature 🎮")
    st.write("Welcome to the Gamification Page! Earn points and badges by completing challenges.")

    # Display points
    st.write(f"**Points:** {st.session_state.points}")
    
    # Display badges
    display_badges()

    # Challenge options
    st.write("### Challenges")
    challenge_type = st.selectbox("Choose a challenge type:", ["Select a challenge", "Classify 5 items", "Learn about recycling", "Participate in a community clean-up"])

    if st.button("Complete Challenge"):
        complete_challenge(challenge_type)

    # Leaderboard section
    st.write("### Leaderboard")
    display_leaderboard()

    # Reset points and badges button
    if st.button("Reset Progress"):
        reset_progress()

# Function to display earned badges
def display_badges():
    st.write("**Badges Earned:**")
    if st.session_state.badges:
        for badge in st.session_state.badges:
            st.markdown(f"- {badge}")
    else:
        st.write("No badges earned yet.")

# Function to complete a challenge
def complete_challenge(challenge_type):
    if challenge_type == "Classify 5 items":
        challenge_points = 15
        st.session_state.points += challenge_points
        st.session_state.badges.append("Waste Classifier!")
        st.success(f"You earned {challenge_points} points for classifying 5 items! 🎉")
    elif challenge_type == "Learn about recycling":
        challenge_points = 10
        st.session_state.points += challenge_points
        st.session_state.badges.append("Recycling Expert!")
        st.success(f"You earned {challenge_points} points for learning about recycling! 📚")
    elif challenge_type == "Participate in a community clean-up":
        challenge_points = 20
        st.session_state.points += challenge_points
        st.session_state.badges.append("Community Hero!")
        st.success(f"You earned {challenge_points} points for participating in a clean-up! 🌍")
    else:
        st.warning("Please select a challenge type.")

    update_leaderboard()

# Function to display leaderboard
def display_leaderboard():
    leaderboard = st.session_state.leaderboard
    if leaderboard:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        for user, points in sorted_leaderboard:
            st.markdown(f"- {user}: **{points} points**")
    else:
        st.write("No users on the leaderboard yet.")

# Function to update the leaderboard
def update_leaderboard():
    username = st.text_input("Enter your name:", "")
    if username and username not in st.session_state.leaderboard:
        st.session_state.leaderboard[username] = st.session_state.points

# Function to reset points and badges
def reset_progress():
    st.session_state.points = 0
    st.session_state.badges = []
    st.session_state.leaderboard = {}
    st.success("Your progress has been reset! 🎮")

