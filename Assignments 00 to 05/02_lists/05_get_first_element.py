import streamlit as st

# Function to get the first element of a list
def get_first_element(lst):
    st.write("The first element in the list is:", lst[0])

# Streamlit UI
st.title("Get First Element from List")

# Initialize an empty list
user_list = []

# Take input from the user for list elements
num_elements = st.number_input("How many elements do you want to enter?", min_value=1, step=1)

for i in range(int(num_elements)):
    element = st.text_input(f"Enter element {i+1}:")
    if element:
        user_list.append(element)

# Display the first element if the list is not empty
if user_list:
    get_first_element(user_list)
