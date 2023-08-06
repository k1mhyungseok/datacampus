#easyocr활용 이후 텍스트에서 숫자, 영어, 특수문자를 제거하고 유의미한 메뉴 이름만 출력하는 코드 포함되어 있음
#python을 활용해 구현
#다만, '순두부'인데 '순 두부'로 출력되거나, '김치찌개'인데 '김 찌 치 개'등의 오타 및 하나의 단어 안에 띄어쓰기로 구분되어 출력되어 맞춤법 수정 필요
#맞춤법 수정 모듈hanspell을 사용했으나 정확도가 떨어지는 것 같음

from PIL import Image, ImageDraw
import easyocr
import numpy as np
import pandas as pd
import re
from hanspell import spell_checker

def clean_text(inputString):
  re_text = re.sub(r'[0-9\.,\s,A-Z,a-z,-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·,{}]', ' ', inputString)
  return re_text

count = 0

while(1):
    route = input("사진의 경로를 입력하세요: ")
    # route = r'C:/team2_prj/ex_menu.jpg'
    reader = easyocr.Reader(['ko'], gpu=False)
    result = reader.readtext(route)
    
    df = pd.DataFrame(result)
    text = df[1]
    MenuName = np.array(text)
    MenuName = ' '.join(MenuName)
    MenuName

    re_name = clean_text(MenuName)
    re_name = ' '.join(re_name.split())
    
    spelled = spell_checker.check(re_name)
    checked_sent = spelled.checked
    print(checked_sent)

    count +=1

    if count > 0:
        break