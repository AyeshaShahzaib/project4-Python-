import streamlit as st

fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
celsius = (fahrenheit - 32) * 5.0 / 9.0
st.write("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")