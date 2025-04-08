import streamlit as st

st.title("Square Calculator")

number = st.number_input("Type a number to see its square:", step=0.1)

if number:
    square = number * number
    st.write(f"{number} squared is {square}")