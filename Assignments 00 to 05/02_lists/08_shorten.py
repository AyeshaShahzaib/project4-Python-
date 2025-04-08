import streamlit as st

MAX_LENGTH = 3  # Required maximum length of the list

def shorten(lst):
    """Removes elements from the end of lst until it is MAX_LENGTH items long."""
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        st.write(f"Removed: {removed_item}")

# Streamlit UI
st.title("Shorten a List to MAX_LENGTH")

# Take user input for list elements
num_elements = st.number_input("How many elements do you want to enter?", min_value=1, step=1)
user_list = [st.text_input(f"Enter element {i+1}:") for i in range(int(num_elements))]

# Filter out empty inputs
user_list = [element for element in user_list if element]

# Display the original list
st.write("Original List:", user_list)

# Process and display the shortened list
if st.button("Shorten List"):
    shorten(user_list)
    st.write("Final List:", user_list)
