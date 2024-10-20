import streamlit as st
import random
import time

# Custom CSS for styling the page
def load_css():
    st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
        color: #4caf50;
    }
    .challenge {
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .badge {
        background-color: #ffd54f;
        border-radius: 15px;
        padding: 5px 10px;
        font-size: 1em;
        margin-right: 5px;
    }
    .leaderboard {
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .milestone {
        color: #2196f3;
        font-weight: bold;
    }
    button {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }
    button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to show the gamification page
def show_gamification_page():
    load_css()  # Load custom CSS styles

    # Initialize session state for user profile, points, badges, challenges, and achievements
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'points' not in st.session_state:
        st.session_state.points = 0
    if 'badges' not in st.session_state:
        st.session_state.badges = []
    if 'challenges' not in st.session_state:
        st.session_state.challenges = {
            "Classify 5 items": False,
            "Learn about recycling": False,
            "Participate in a community clean-up": False,
            "Share on Social Media": False
        }
    if 'milestones' not in st.session_state:
        st.session_state.milestones = []
    if 'leaderboard' not in st.session_state:
        st.session_state.leaderboard = {}

    st.markdown('<h1 class="title">🎮 Gamification Feature</h1>', unsafe_allow_html=True)
    st.write("Welcome to the Gamification Page! Earn points and badges by completing challenges.")

    # User profile input
    if st.session_state.username == '':
        st.session_state.username = st.text_input("Enter your username to start:", "")
        if st.session_state.username:
            st.success(f"Welcome, {st.session_state.username}! Let's start earning points! 🎉")
    else:
        st.write(f"**User:** {st.session_state.username}")

    # Display points and badges
    st.write(f"**Points:** {st.session_state.points}")
    display_badges()

    # Challenge options
    st.write("### Challenges")
    challenge_type = st.selectbox("Choose a challenge type:", 
                                   ["Select a challenge"] + list(st.session_state.challenges.keys()))

    if st.button("Complete Challenge"):
        complete_challenge(challenge_type)

    # Milestones section
    st.write("### Milestones")
    display_milestones()

    # Leaderboard section
    st.write("### Leaderboard")
    display_leaderboard()

    # Reset points and badges button
    if st.button("Reset Progress"):
        reset_progress()

    # Social sharing
    if st.button("Share Your Progress!"):
        st.success("Your progress has been shared on social media! 🎉")  # Placeholder for actual sharing functionality

# Function to display earned badges
def display_badges():
    st.write("**Badges Earned:**")
    badge_container = st.container()
    with badge_container:
        if st.session_state.badges:
            for badge in st.session_state.badges:
                st.markdown(f'<span class="badge">{badge}</span>', unsafe_allow_html=True)
        else:
            st.write("No badges earned yet.")

# Function to complete a challenge
def complete_challenge(challenge_type):
    if challenge_type in st.session_state.challenges:
        if st.session_state.challenges[challenge_type]:
            st.warning("You have already completed this challenge!")
            return

        challenge_points = random.randint(5, 25)  # Random points for variety
        st.session_state.points += challenge_points
        st.session_state.badges.append(f"{challenge_type} Completed! 🎖️")
        st.session_state.challenges[challenge_type] = True
        st.success(f"You earned {challenge_points} points for completing '{challenge_type}'! 🎉")
        show_animation(f"Congratulations on completing '{challenge_type}'!")

        check_milestone()
        update_leaderboard()

# Function to show a simple animation for completion
def show_animation(message):
    with st.spinner("Loading..."):
        time.sleep(1)  # Simulate a loading time
    st.balloons()  # Streamlit built-in function for a fun effect
    st.success(message)
    play_sound_effect()  # Play a sound effect upon completion

# Function to play sound effects (requires sound files to be available)
def play_sound_effect():
    sound_file = "import streamlit as st
import random
import time

# Custom CSS for styling the page
def load_css():
    st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    .title {
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
        color: #4caf50;
    }
    .challenge {
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .badge {
        background-color: #ffd54f;
        border-radius: 15px;
        padding: 5px 10px;
        font-size: 1em;
        margin-right: 5px;
    }
    .leaderboard {
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .milestone {
        color: #2196f3;
        font-weight: bold;
    }
    button {
        background-color: #4caf50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 15px;
        cursor: pointer;
        font-size: 1em;
        transition: background-color 0.3s ease;
    }
    button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to show the gamification page
def show_gamification_page():
    load_css()  # Load custom CSS styles

    # Initialize session state for user profile, points, badges, challenges, and achievements
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'points' not in st.session_state:
        st.session_state.points = 0
    if 'badges' not in st.session_state:
        st.session_state.badges = []
    if 'challenges' not in st.session_state:
        st.session_state.challenges = {
            "Classify 5 items": False,
            "Learn about recycling": False,
            "Participate in a community clean-up": False,
            "Share on Social Media": False
        }
    if 'milestones' not in st.session_state:
        st.session_state.milestones = []
    if 'leaderboard' not in st.session_state:
        st.session_state.leaderboard = {}

    st.markdown('<h1 class="title">🎮 Gamification Feature</h1>', unsafe_allow_html=True)
    st.write("Welcome to the Gamification Page! Earn points and badges by completing challenges.")

    # User profile input
    if st.session_state.username == '':
        st.session_state.username = st.text_input("Enter your username to start:", "")
        if st.session_state.username:
            st.success(f"Welcome, {st.session_state.username}! Let's start earning points! 🎉")
    else:
        st.write(f"**User:** {st.session_state.username}")

    # Display points and badges
    st.write(f"**Points:** {st.session_state.points}")
    display_badges()

    # Challenge options
    st.write("### Challenges")
    challenge_type = st.selectbox("Choose a challenge type:", 
                                   ["Select a challenge"] + list(st.session_state.challenges.keys()))

    if st.button("Complete Challenge"):
        complete_challenge(challenge_type)

    # Milestones section
    st.write("### Milestones")
    display_milestones()

    # Leaderboard section
    st.write("### Leaderboard")
    display_leaderboard()

    # Reset points and badges button
    if st.button("Reset Progress"):
        reset_progress()

    # Social sharing
    if st.button("Share Your Progress!"):
        st.success("Your progress has been shared on social media! 🎉")  # Placeholder for actual sharing functionality

# Function to display earned badges
def display_badges():
    st.write("**Badges Earned:**")
    badge_container = st.container()
    with badge_container:
        if st.session_state.badges:
            for badge in st.session_state.badges:
                st.markdown(f'<span class="badge">{badge}</span>', unsafe_allow_html=True)
        else:
            st.write("No badges earned yet.")

# Function to complete a challenge
def complete_challenge(challenge_type):
    if challenge_type in st.session_state.challenges:
        if st.session_state.challenges[challenge_type]:
            st.warning("You have already completed this challenge!")
            return

        challenge_points = random.randint(5, 25)  # Random points for variety
        st.session_state.points += challenge_points
        st.session_state.badges.append(f"{challenge_type} Completed! 🎖️")
        st.session_state.challenges[challenge_type] = True
        st.success(f"You earned {challenge_points} points for completing '{challenge_type}'! 🎉")
        show_animation(f"Congratulations on completing '{challenge_type}'!")

        check_milestone()
        update_leaderboard()

# Function to show a simple animation for completion
def show_animation(message):
    with st.spinner("Loading..."):
        time.sleep(1)  # Simulate a loading time
    st.balloons()  # Streamlit built-in function for a fun effect
    st.success(message)
    play_sound_effect()  # Play a sound effect upon completion

# Function to play sound effects (requires sound files to be available)
def play_sound_effect():
    sound_file = "applause-cheer-236786.mp3"  # Replace with the path to your sound file
    try:
        st.audio(sound_file)
    except Exception as e:
        st.error(f"Error playing sound: {e}")

# Function to display milestones
def display_milestones():
    st.write("**Milestones Achieved:**")
    milestone_container = st.container()
    with milestone_container:
        if st.session_state.milestones:
            for milestone in st.session_state.milestones:
                st.markdown(f'<span class="milestone">{milestone}</span>', unsafe_allow_html=True)
        else:
            st.write("No milestones achieved yet.")

# Function to check and add milestones
def check_milestone():
    milestones = [
        (50, "50 Points Milestone 🎖️"),
        (100, "100 Points Milestone 🎖️"),
        (200, "200 Points Milestone 🎖️"),
    ]
    for point, milestone in milestones:
        if st.session_state.points >= point and milestone not in st.session_state.milestones:
            st.session_state.milestones.append(milestone)
            st.success(f"Congratulations! You've reached {point} points!")

# Function to display leaderboard
def display_leaderboard():
    if st.session_state.leaderboard:
        sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
        st.write("### Top Players:")
        leaderboard_container = st.container()
        with leaderboard_container:
            for user, points in sorted_leaderboard:
                st.markdown(f"- **{user}**: {points} points")
    else:
        st.write("No users on the leaderboard yet.")

# Function to update the leaderboard
def update_leaderboard():
    username = st.session_state.username
    st.session_state.leaderboard[username] = st.session_state.points

# Function to reset points and badges
def reset_progress():
    st.session_state.points = 0
    st.session_state.badges = []
    st.session_state.challenges = {
        "Classify 5 items": False,
        "Learn about recycling": False,
        "Participate in a community clean-up": False,
        "Share on Social Media": False
    }
    st.session_state.milestones = []
    st.session_state.leaderboard = {}
    st.success("Your progress has been reset! 🎮")

# Call the function to show the gamification page
if __name__ == "__main__":
    show_gamification_page()
"  # Replace with the path to your sound file
    try:
        st.audio(sound_file)
    except Exception as e:
        st.error(f"Error playing sound: {e}")

# Function to display milestones
def display_milestones():
    st.write("**Milestones Achieved:**")
    milestone_container = st.container()
    with milestone_container:
        if st.session_state.milestones:
            for milestone in st.session_state.milestones:
                st.markdown(f'<span class="milestone">{milestone}</span>', unsafe_allow_html=True)
        else:
            st.write("No milestones achieved yet.")

# Function to check and add milestones
def check_milestone():
    milestones = [
        (50, "50 Points Milestone 🎖️"),
        (100, "100 Points Milestone 🎖️"),
        (200, "200 Points Milestone 🎖️"),
    ]
    for point, milestone in milestones:
        if st.session_state.points >= point and milestone not in st.session_state.milestones:
            st.session_state.milestones.append(milestone)
            st.success(f"Congratulations! You've reached {point} points!")

# Function to display leaderboard
def display_leaderboard():
    if st.session_state.leaderboard:
        sorted_leaderboard = sorted(st.session_state.leaderboard.items(), key=lambda x: x[1], reverse=True)
        st.write("### Top Players:")
        leaderboard_container = st.container()
        with leaderboard_container:
            for user, points in sorted_leaderboard:
                st.markdown(f"- **{user}**: {points} points")
    else:
        st.write("No users on the leaderboard yet.")

# Function to update the leaderboard
def update_leaderboard():
    username = st.session_state.username
    st.session_state.leaderboard[username] = st.session_state.points

# Function to reset points and badges
def reset_progress():
    st.session_state.points = 0
    st.session_state.badges = []
    st.session_state.challenges = {
        "Classify 5 items": False,
        "Learn about recycling": False,
        "Participate in a community clean-up": False,
        "Share on Social Media": False
    }
    st.session_state.milestones = []
    st.session_state.leaderboard = {}
    st.success("Your progress has been reset! 🎮")

# Call the function to show the gamification page
if __name__ == "__main__":
    show_gamification_page()
