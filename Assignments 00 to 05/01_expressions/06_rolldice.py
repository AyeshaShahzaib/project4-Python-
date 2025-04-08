import streamlit as st
import random

st.title("Dice Roller")

if st.button("Roll the Dice"):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    st.write(f"🎲 Die 1: {die1}")
    st.write(f"🎲 Die 2: {die2}")
    st.write(f"🔢 Total: {total}")