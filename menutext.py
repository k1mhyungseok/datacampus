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