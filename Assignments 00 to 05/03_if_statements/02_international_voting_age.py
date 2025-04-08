import streamlit as st

st.title("Can You Vote? 🗳️")

# Get user's age
age = st.number_input("How old are you?", min_value=0, step=1)

# Define voting ages
voting_ages = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

# Check voting eligibility
for country, required_age in voting_ages.items():
    if age >= required_age:
        st.write(f"✅ You can vote in {country} where the voting age is {required_age}.")
    else:
        st.write(f"❌ You cannot vote in {country} where the voting age is {required_age}.")
