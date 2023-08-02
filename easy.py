import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
import easyocr

def ocr_image(image_path, lang='ko'):
    reader = easyocr.Reader([lang])
    image = Image.open(image_path)
    result = reader.readtext(image)
    return result

def main():
    st.title('메뉴판 OCR 분석')

    uploaded_file = st.file_uploader("메뉴 사진을 업로드해주세요.", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            ## OCR 분석을 시작하기 전에 progress bar 생성
            progress_bar = st.progress(0)

            result = ocr_image(uploaded_file)

            ## OCR 분석 완료 후 progress bar를 100%로 설정
            progress_bar.progress(100)
            st.success("Done")

            st.subheader("원하는 결과를 선택하세요")
            for r in result:
                st.text(f"텍스트: {r[1]}")
                
                
        except Exception as e:
            st.error(f"오류오류오류오류: {e}")


if __name__ == "__main__":
    main()