import streamlit as st
import numpy as np
import pandas as pd

st.title('choice')
st.button('삼겹살')

if st.button('삽겹살'):
    st.write('hello,streamlit!')

if st.checkbox('감자탕'):
    st.text('정보')
else:
    st.text('hide')

