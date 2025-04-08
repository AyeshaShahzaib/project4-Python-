import streamlit as st

st.title("Favorite Animal App")

favorite_animal = st.text_input("What's your favorite animal?")

if favorite_animal:
    st.write("My favorite animal is also " + favorite_animal + "!")