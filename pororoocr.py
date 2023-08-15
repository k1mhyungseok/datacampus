import streamlit as st
import pandas as pd
from PIL import Image
from pororo import Pororo
import os
import re

ocr = Pororo(task='ocr', lang='ko')

def clean_text(inputString):
    re_text = re.sub(r'[0-9\.,\s,A-Z,a-z,-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·,{}]', ' ', inputString)
    return re_text

def main():
    st.title('메뉴판 OCR 분석')

    uploaded_file = st.file_uploader("메뉴 사진을 업로드해주세요.", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # uploads 폴더 생성
            if not os.path.exists('uploads'):
                os.makedirs('uploads')

            # 업로드된 이미지 파일 저장
            image_path = os.path.join('uploads', uploaded_file.name)
            with open(image_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            # OCR 분석을 시작하기 전에 progress bar 생성
            progress_bar = st.progress(0)

            result = ocr(image_path)

            # OCR 분석 완료 후 progress bar를 100%로 설정
            progress_bar.progress(100)
            st.success("Done")

            st.subheader("원하는 결과를 선택하세요")

            data = []

            for r in result:
                cleaned_result = clean_text(r)
                resultz = cleaned_result.split()  # 띄어쓰기를 기준으로 분리
                data.extend(resultz)

            df = pd.DataFrame(data, columns=["결과"])
            st.table(df)

            # OCR이 끝난 후 파일 삭제
            os.remove(image_path)

        except Exception as e:
            st.error(f"오류: {e}")

if __name__ == "__main__":
    main()