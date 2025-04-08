import streamlit as st

# Constant for the speed of light
C = 299792458  

st.title("Mass-Energy Equivalence Calculator")

mass = st.number_input("Enter kilos of mass:", min_value=0.0, format="%.2f")

if mass > 0:
    energy = mass * C**2
    st.write("e = m * C^2...")
    st.write(f"m = {mass} kg")
    st.write(f"C = {C} m/s")
    st.write(f"{energy:.2e} joules of energy!")