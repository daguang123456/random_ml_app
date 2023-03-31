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
    st.title("随机数字颜色")

    st.header("随机数字r")
    number = generate_random_number()
    st.write(f"得出: {number}")

    st.header("随机颜色")
    color = generate_random_color()
    st.write(f"得出: {color}")
    st.markdown(f"<div style='background-color: {color}; width: 50px; height: 50px;'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
