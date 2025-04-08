import streamlit as st

st.title("Division and Remainder Calculator")

num1 = st.number_input("Please enter an integer to be divided:", step=1, format="%d")
num2 = st.number_input("Please enter an integer to divide by:", step=1, format="%d", min_value=1)

if num1 and num2:
    quotient = num1 // num2
    remainder = num1 % num2
    st.write(f"The result of this division is {quotient} with a remainder of {remainder}")