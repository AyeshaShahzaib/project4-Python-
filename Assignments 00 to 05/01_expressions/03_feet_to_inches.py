import streamlit as st

st.title("Feet to Inches Converter")

feet = st.number_input("Enter length in feet:", min_value=0.0, format="%.2f")

if feet > 0:
    inches = feet * 12
    st.write(f"{feet} feet is equal to {inches} inches.")