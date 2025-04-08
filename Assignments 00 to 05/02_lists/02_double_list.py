import streamlit as st

def double_numbers(numbers):
    return [num * 2 for num in numbers]

st.title("Double Each Number")

# Get user input as a comma-separated string
numbers_input = st.text_input("Enter numbers separated by commas:")

if numbers_input:
    try:
        numbers_list = [float(num.strip()) for num in numbers_input.split(",")]
        doubled_list = double_numbers(numbers_list)
        st.write(f"Doubled numbers: {doubled_list}")
    except ValueError:
        st.write("Please enter valid numbers separated by commas.")
