import streamlit as st

# Pre-specified minimum height requirement
MIN_HEIGHT = 50

st.title("Rollercoaster Height Check")

# Function to check if the user is tall enough to ride
def check_height(height):
    if height >= MIN_HEIGHT:
        return "You're tall enough to ride!"
    else:
        return "You're not tall enough to ride, but maybe next year!"

# Ask for height input
height = st.number_input("How tall are you?", min_value=0)

# Display message based on the user's height
if height:
    result = check_height(height)
    st.write(result)
else:
    st.write("Please enter a valid height!")
