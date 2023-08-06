import streamlit as st
import numpy as np
import pandas as pd

if st.button('삽겹살'):
    col1, col2 = st.columns([1,1])

    with col1:
        st.text("한국어_이름")
        st.text("번역이름(영어 및 로마자)")
    
    with col2:
        st.text("관련 정보")
        st.text("링크연결")

if st.button('된장찌개'):
    col1, col2 = st.columns([1,1])

    with col1:
        st.text("한국어_이름")
        st.text("번역이름(영어 및 로마자)")
    
    with col2:
        st.text("관련 정보")
        st.text("링크연결")
        
if st.button('순두부'):
    col1, col2 = st.columns([1,1])

    with col1:
        st.text("한국어_이름")
        st.text("번역이름(영어 및 로마자)")
    
    with col2:
        st.text("관련 정보")
        st.text("링크연결")


if st.checkbox('감자탕'):
    st.text('정보')
else:
    st.text('hide')
    st.text('hide2')

