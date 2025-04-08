import streamlit as st

st.title("Leap Year Checker")

# Get the year input from the user
year = st.number_input("Enter a year to check if it's a leap year:", min_value=1)

# Function to check for a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Check if the year is a leap year
if is_leap_year(year):
    st.write("That's a leap year!")
else:
    st.write("That's not a leap year.")
