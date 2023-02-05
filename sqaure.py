import streamlit as st
st.title("SQUARE OF NUMBERS")
st.markdown("Slide to get square of the number")
x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

