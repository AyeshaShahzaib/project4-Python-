import streamlit as st

# Constants
DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTE = 60

# Calculation
seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

st.title("Seconds in a Year Calculator")
st.write(f"There are {seconds_in_year} seconds in a year!")