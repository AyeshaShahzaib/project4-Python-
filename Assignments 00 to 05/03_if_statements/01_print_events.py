import streamlit as st

st.title("First 20 Even Numbers")

# Generate the first 20 even numbers
even_numbers = [i * 2 for i in range(20)]

# Display the even numbers
st.write("The first 20 even numbers are:")
st.write(" ".join(map(str, even_numbers)))
