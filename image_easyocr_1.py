#사용자에게 이미지의 경로를 input 받아서 easyocr로 텍스트를 인식하여 dataframe으로 텍스트만 출력되게 구현
#python과 여러 모듈로 구현했으며, 단어의 정확도 및 stopwords는 반영되지 않았음
#input에 컴퓨터에 있는 이미지의 이름을 입력해야 한다는 한계점 존재

from PIL import Image, ImageDraw
import os
import cv2 as cv
import easyocr
import numpy as np
import pandas as pd

count = 0

while(1):
    route = input("사진의 경로를 입력하세요: ")
    # route = r'C:/team2_prj/ex_img.png'
    reader = easyocr.Reader(['ko'], gpu=False)
    result = reader.readtext(route)
    result2 = reader.readtext(route, detail=0)
    print(result)
    print(result2)

    df = pd.DataFrame(result)
    print(df)

    df2 = pd.DataFrame(result2)
    print(df2)
    
    count +=1

    if count > 0:
        break