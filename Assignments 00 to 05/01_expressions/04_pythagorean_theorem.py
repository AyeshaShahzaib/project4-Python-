import streamlit as st
import math

st.title("Pythagorean Theorem Calculator")

ab = st.number_input("Enter the length of AB:", min_value=0.0, format="%.2f")
ac = st.number_input("Enter the length of AC:", min_value=0.0, format="%.2f")

if ab > 0 and ac > 0:
    bc = math.sqrt(ab**2 + ac**2)
    st.write(f"The length of BC (the hypotenuse) is: {bc:.2f}")
