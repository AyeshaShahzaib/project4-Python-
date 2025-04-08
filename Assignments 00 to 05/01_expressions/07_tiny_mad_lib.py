import streamlit as st

st.title("Mad Libs Game")

# Get user inputs
adjective = st.text_input("Please type an adjective and press enter:")
noun = st.text_input("Please type a noun and press enter:")
verb = st.text_input("Please type a verb and press enter:")

if adjective and noun and verb:
    st.write(f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!")