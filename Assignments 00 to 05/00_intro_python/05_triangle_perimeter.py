import streamlit as st

st.title("Triangle Perimeter Calculator")

side1 = st.number_input("What is the length of side 1?", min_value=0.0, step=0.1)
side2 = st.number_input("What is the length of side 2?", min_value=0.0, step=0.1)
side3 = st.number_input("What is the length of side 3?", min_value=0.0, step=0.1)

if side1 > 0 and side2 > 0 and side3 > 0:
    perimeter = side1 + side2 + side3
    st.write(f"The perimeter of the triangle is {perimeter}")