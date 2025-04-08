import streamlit as st

# Function to get the last element of a list
def get_last_element(lst):
    st.write("The last element in the list is:", lst[-1])

# Streamlit UI
st.title("Get Last Element from List")

# Take input from the user for list elements
num_elements = st.number_input("How many elements do you want to enter?", min_value=1, step=1)

# Store inputs dynamically in a list
user_list = [st.text_input(f"Enter element {i+1}:") for i in range(int(num_elements))]

# Filter out empty inputs
user_list = [element for element in user_list if element]

# Display the last element if the list is not empty
if user_list:
    get_last_element(user_list)
