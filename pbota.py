import streamlit as st
from PIL import Image
from pororo import Pororo
import os
import requests
import json
import requests
import json
from pprint import pprint  #python에서 json 파일 보기 좋게 만드는 import
import re

ocr = Pororo(task='ocr', lang='ko')

# 오타 수정 딕셔너리
typo_correction = {
    "봉인" : ["뽕잎"],
    "봉인 보쌈" : ["뽕잎 보쌈"],
    "수저 등심 돈 가스" : ["수제등심돈까스"],
    "돈가스" : ["돈까스"],
    "치즈돈가스" : ["치즈돈까스"],
    "함박 가스" : ["함박까스"],


}

def correct_typo(menu):
    if menu in typo_correction:
        return typo_correction[menu][0]
    return menu

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

            # result를 text 파일로 저장하기(부산대 시작)
            file = open("result.txt", "w", encoding='utf-8')
            file.write("\n".join(result))
            file.close()

            # 1. 텍스트 준비 & 개행문자 처리
            with open('result.txt', 'r', encoding='utf-8') as f:
                text = f.read()
            text = text.replace('\n', '\r\n')
            # 2. 맞춤법 검사 요청 (requests)
            response = requests.post('http://164.125.7.61/speller/results', data={'text1': text})
            # 3. 응답에서 필요한 내용 추출 (html 파싱)
            data = response.text.split('data = [', 1)[-1].rsplit('];', 1)[0]
            # 4. 파이썬 딕셔너리 형식으로 변환
            data = json.loads(data)

            # OCR 분석 완료 후 progress bar를 100%로 설정
            progress_bar.progress(100)
            st.success("Done")

            st.subheader("원하는 결과를 선택하세요")

            # 5. 교정 내용 출력
            for err in data['errInfo']:
                cand_words = err.get('candWord', '')  # 'candWord'가 없는 경우 빈 문자열로 초기화
                first_cand_word = cand_words.split('|')[0] if '|' in cand_words else cand_words  #can_words내에 |가 있으면 그 앞의 단어만 출력 그 외엔 그냥 출력
                corrected_word = correct_typo(first_cand_word)
                
                # 숫자만 있는 부분은 제외, 특수문자, 영어 대문자 알파벳 한자리만 있는 경우 제외
                if re.sub(r'[0-9\.,\s,A-Z,-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·,{}]', '', text) == '':
                    continue

                st.text(f"결과 : {corrected_word}")

            # OCR이 끝난 후 파일 삭제
            os.remove(image_path)

        except Exception as e:
            st.error(f"에러남 : {e}")

if __name__ == "__main__":
    main()