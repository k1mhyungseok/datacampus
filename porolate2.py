import streamlit as st
import pandas as pd
from PIL import Image
from pororo import Pororo
import os
import re

ocr = Pororo(task='ocr', lang='ko')

# 오타 수정 딕셔너리
# 일부단어 추가 
typo_correction = {
    "김치 참치주먹밥" : ["김치참치주먹밥"],
    "사이드 메뉴" : ["사이드메뉴"],
    "꽃방 추가" : ["꽃빵추가"],
    "돈가스" : ["돈까스"],
    "얼큰샤브칼 국수" : ["얼큰샤브칼국수"],
    "맑은샤브칼 국수" : ["맑은샤브칼국수"],
    "얼큰샤브칼" : ["얼큰샤브칼국수"],
    "맑은샤브칼" : ["맑은샤브칼국수"],
    "꽃방" : ["꽃빵"],
    "낙지" : ['산낙지'],
    "오징어구이" : ["마른오징어구이"],
    "해" : ["해삼"],
    "전" : ["전복"],
    "옥" : ['전복'],
    "음료 수" : ["음료수"],
    "응심이만두" : ["옹심이만두"],
    "소고기 미나리 버섯 칼국수 볶음밥" : ["소고기미나리버섯칼국수볶음밥"],
    "곱장어" : ["꼼장어"],
    "산 낙지" : ["산낙지"],
    "두부 김치" : ["두부김치"],
    "바다 장어" : ["바다장어"],
    "마른 마리 오징어구이" : ["마른오징어구이"],
    "대합방" : ["대합탕"],
    "삐들이" : ["삐둘이"],
    "전 옥" : ["전복"],
    "해 샥" : ["해삼"],
    "토마토계란" : ["토마토계란볶음"],
    "볶음" : ["토마토계란볶음"],
    "간풍육" : ["깐풍육"],
    "간쇼새우" : ["깐쇼새우"],
    "간소새우" : ["깐쇼새우"],
    "간풍새우" : ["깐풍새우"],
    "애물녹두빈대떡" : ["해물녹두빈대떡"],
    "굴회무힘" : ["굴회무침"],
    "맥" : ["맥주"],
    "주" : ["맥주"]

}

#stopwords 리스트
stopword=['볶음요리','속','다','요리료','중국요리전문점','야','냐','기','지지','소기지','구속씨','추',
        '작권권단','장기자장장구구','간고고고고고고고','녹두류','파전류','전','료','계절메뉴','스페셜',
        '특','국내산','재료만','사용합니다','어서오세요','인이상','국수','추가메뉴','주류','음료','수',
       '식사','원','추가','사이드','메뉴','예약메뉴','추가','개','식사','요리는','데워드리지','않습니다',
       '삼선탐외에','차림표','산','마리','마른','마리','삐둘이','샥']

def correct_typo(menu):
    if menu in typo_correction:
        return typo_correction[menu][0]
    return menu

def clean_text(inputString):
    re_text = re.sub(r'[^\uAC00-\uD7A3]', ' ', inputString)
    return re_text

def ocrmain():
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
                corrected_result = [correct_typo(menu) for menu in resultz]  # 오타 수정 적용
                data.extend(corrected_result)

            menu_df = pd.DataFrame(data, columns=["결과"])

            #st.table(menu_df)  웹에서 안 보입니당

            menu_lst = menu_df["결과"].tolist()  # "결과" 컬럼 값을 리스트로 저장
            print("stopword 제거 전 :", menu_lst) #콘솔에서 출력

            #불용어제거 
            menu_lst_last = []
            
            for w in menu_lst:
                if w not in stopword:
                    menu_lst_last.append(w)

            #중복되는 메뉴명 없애고 다시 리스트화, 순서 뒤바뀌긴 함
            menu_lst_last = list(set(menu_lst_last))

            print("stoprword 제거 후: ", menu_lst_last)  #streamlit에 넘길 때 menu_lst_last 넘겨야 함

            # OCR이 끝난 후 파일 삭제
            os.remove(image_path)

        except Exception as e:
            st.error(f"오류: {e}")

if __name__ == "__main__":
    ocrmain()


