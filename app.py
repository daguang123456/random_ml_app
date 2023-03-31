import streamlit as st
import random

def generate_random_number():
    return random.randint(1, 100)

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

def main():
    st.title("Random Machine Learning App")

    st.header("Random Number")
    number = generate_random_number()
    st.write(f"The generated number is: {number}")

    st.header("Random Color")
    color = generate_random_color()
    st.write(f"The generated color is: {color}")
    st.markdown(f"<div style='background-color: {color}; width: 50px; height: 50px;'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
