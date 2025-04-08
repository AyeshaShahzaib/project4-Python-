import streamlit as st
import random

st.title("Dice Roll Simulator")

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

st.write("Rolling two dice three times...")

for i in range(1, 4):
    die1, die2 = roll_dice()
    st.write(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")