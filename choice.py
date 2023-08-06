#메뉴판의 음식 이름을 인식하고 버튼 혹은 체크박스를 활용해 사용자가 정보를 확인하고 싶은 메뉴를 선택할 수 있는 UI 제공
#streamlit을 활용하여 구현했으며, 버튼/체크박스 중 하나의 형식을 선택할 예정
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

