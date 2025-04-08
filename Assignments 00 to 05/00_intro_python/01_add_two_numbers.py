import streamlit as st

st.title("Simple Addition App")

num1 = st.number_input("Enter the first number:", value=0, step=1)
num2 = st.number_input("Enter the second number:", value=0, step=1)

if st.button("Calculate Sum"):
    result = num1 + num2
    st.success(f"The sum is: {result}")