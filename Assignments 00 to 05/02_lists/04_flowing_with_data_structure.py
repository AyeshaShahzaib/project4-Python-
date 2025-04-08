import streamlit as st

# Function to add three copies of data to a list
def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

# Streamlit UI
st.title("Mutability Demo: Lists vs. Numbers")

# User input
message = st.text_input("Enter a message to copy:")

# Initialize an empty list
data_list = []

# Show list before modification
st.write("List before:", data_list)

# Add three copies if the user has entered something
if message:
    add_three_copies(data_list, message)
    st.write("List after:", data_list)
