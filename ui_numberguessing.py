import streamlit as st
from numberguessing import create_number, get_guess

st.title("Number Guessing Game")
st.write("Guess the number between 1 and 100!")

if 'secret_number' not in st.session_state:
    st.session_state ['secret_number'] = create_number()

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
guess_button = st.button("Guess")

if guess_button:
    if guess:
        result = get_guess(guess, st.session_state['secret_number'])
        st.write(result)
        
        if result == "Selamat! Kamu berhasil menebak angka!":
            st.session_state['secret_number'] = create_number()
            st.success("A new number has been generated!")
    else:
        st.warning("Please enter a number before guessing.")