import streamlit as st
from PIL import Image
import easyocr
import pandas as pd
import numpy as np
import re

## easyocr
def ocr_image(image_path, lang='ko'):
    reader = easyocr.Reader([lang])
    image = Image.open(image_path)
    result = reader.readtext(image)
    return result

def main():
    st.title('메뉴판 이미지 분석')

    uploaded_file = st.file_uploader("메뉴 사진을 업로드해주세요.", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            #### easyocr 시작하기 전에 progress bar 생성
            progress_bar = st.progress(0)

            #### easyocr 진행
            result = ocr_image(uploaded_file)

            #### easyocr 완료 후 progress bar를 100%로 설정
            progress_bar.progress(100)
            
            #### progress bar 100%시 완료 문구 
            st.success("Done")

            st.subheader("원하는 결과를 선택하세요")

            #### 하나씩 출력
            for r in result:
                top_left, top_right, bottom_right, bottom_left = r[0]
                text = r[1]
                left = min(top_left[0], bottom_left[0])
                top = min(top_left[1], top_right[1])
                right = max(bottom_right[0], top_right[0])
                bottom = max(bottom_right[1], bottom_left[1])

                #### 숫자만 있는 부분은 제외, 특수문자, 영어 대문자 알파벳 한자리만 있는 경우 제외
                if re.sub(r'[0-9\.,\s,A-Z,-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·,{}]', '', text) == '':
                    continue

                #### 결과
                st.text(f"텍스트: {text}")
                st.image(Image.open(uploaded_file).crop((left, top, right, bottom)), caption=f"{text}")

        except Exception as e:
            st.error(f"오류오류오류: {e}")


if __name__ == "__main__":
    main()
