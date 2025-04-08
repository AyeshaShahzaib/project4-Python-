import streamlit as st

def sum_of_numbers(numbers):
    return sum(numbers)

st.title("Sum of Numbers")

# Get user input as a comma-separated string
numbers_input = st.text_input("Enter numbers separated by commas:")

if numbers_input:
    try:
        numbers_list = [float(num.strip()) for num in numbers_input.split(",")]
        result = sum_of_numbers(numbers_list)
        st.write(f"The sum of the entered numbers is: {result}")
    except ValueError:
        st.write("Please enter valid numbers separated by commas.")
