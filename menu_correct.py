import easyocr
import requests
import json
from pprint import pprint
import numpy as np
import pandas as pd
import re

###숫자, 특수문자, 영어 제거 함수
def clean_text(inputString):
    re_text = re.sub(r'[0-9\.,\s,A-Z,a-z,-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·,{}]', ' ', inputString)
    return re_text

###easyocr 적용

count = 0

while(1):
    route = input("사진의 경로를 입력하세요: ")
    # route = r'C:/team2_prj/ex_menu.jpg
    reader = easyocr.Reader(['ko'], gpu=False)
    result = reader.readtext(route)
    
    df = pd.DataFrame(result)
    text = df[1]
    MenuName = np.array(text)
    MenuName = ' '.join(MenuName)
    MenuName

    re_name = clean_text(MenuName)
    re_name = ' '.join(re_name.split())
    print(re_name)  
    #print(type(re_name))   #data형: str

    count +=1

    if count > 0:
        break

###아래 작업을 해야만 밑에 코드 작동

#re_name을 text 파일로 저장
file = open("rename.txt", "w", encoding='UTF8')
file.write(re_name)
file.close()

#최초의 rename.text
# with open("C:\Personal_prj\\rename.txt", 'w', encoding='utf-8') as f:
#     data= "점심특선 김치피개 미마 부대피개 미마 된장피개 마마 돈 가 스 마마 낙지뒷밥 제육볶음 계 칸 짐 라면사리"
#     f.write(data)

#단어 사이 띄어진 것 붙이기 및 무의미한 불용어(미마) 지우고 같은 이름으로 다시 저장
#위의 rename.text와 달라짐
with open("C:\Personal_prj\\rename.txt",'w', encoding = 'utf-8') as f:
    data = "점심특선 김치피개 부대피개 된장피개 돈가스 낙지뒷밥 제육볶음 계칸짐 라면사리"
    f.write(data)

###################################################################중요###########################################################################
#re_name 파일을 열람할 수 있고 요소에 접근 가능
#근데... 이게 가능하니까 애초에 여기에서 그냥 오타가 미흡한 단어 우리가 고치고 다시 저장하면 되긴 함..
##################################################################################################################################################
#anyway, 일단 맞춤법 검사기 적용 및 그것만 출력하는 거 해보겠음


####부산대 맞춤법 검사기 적용

# 1. 텍스트 준비 & 개행문자 처리
with open('rename.txt', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('\n', '\r\n')
# 2. 맞춤법 검사 요청 (requests)
response = requests.post('http://164.125.7.61/speller/results', data={'text1': text})
# 3. 응답에서 필요한 내용 추출 (html 파싱)
data = response.text.split('data = [', 1)[-1].rsplit('];', 1)[0]
# 4. json 딕셔너리 형식으로 변환
data = json.loads(data)
# print(type(data))  #class 'dict'
# 5. 교정 내용 출력
# pprint(data['errInfo'])


###오타 고치는 dataframe, dictionary
#형식) '우리가 원하는 단어':['오타 예측 가능 단어 모음']
#dataframe의 경우, []안의 개수 똑같게
correction_df = pd.DataFrame({'김치찌개':['김치피게', '김찌치개', '김치 피게','김치피개', '김치 피개'],
                                '부대찌개':['부대피개', '부대 피개', '부대피게', '부대피게','부데피개'],
                                '된장찌개':['된장피개', '된장 피개', '된장피게', '된장 피게', '된장피기'],
                             '낙지덮밥':['낙지뒷밥', '낙지됫밥','낙지둣밥', '낙지딧밥', '낙지됩밥'],
                                '계란찜':['계칸찜', '개란찜' , '개칸짐', '게칸짐', '계칸짐']})

correction = {'김치찌개':['김치피게', '김찌치개', '김치 피게','김치피개', '김치 피개'],
                 '부대찌개':['부대피개', '부대 피개', '부대피게', '부대피게'],
                 '된장찌개':['된장피개', '된장 피개', '된장피게', '된장 피게'],
                 '낙지덮밥':['낙지뒷밥', '낙지됫밥','낙지둣밥', '낙지딧밥', '낙지됩밥','낙지둡밥'],
                 '계란찜':['계칸찜', '개란찜' ,'계롼쮬','개란찜', '개칸짐', '게칸짐', '계칸짐']}

# print(list(correction.keys()))  #딕셔너리의 키값들만 리스트로 변환
# print(list(correction.values()))  #딕셔너리의 값들만 리스트로 변환
lst_key = list(correction.keys())   #1차원 배열
lst_value = list(correction.values())   #2차원 배열


### 2차원 배열인 lst_value 하나씩 돌면서 err['orgStr']이랑 맞는 게 있으면 그 단어 출력
#err['orgStr']이란 rename.txt 파일에 있는 단어들과 같은 단어(대치어 아님)
findtext = []
for err in data['errInfo']:
    for i in lst_value:
        for j in i:
            if err['orgStr'] == j:
                findtext.append(j)


###위에서 찾은 오타 단어 리스트와 dataframe의 값끼리 비교하고 해당되는 단어가 있으면 그 단어의 열 이름으로 치환
#join함수로 index를 문자열로 바꿈
for text in findtext:
    if text == correction_df.values.all():
        text = correction_df.columns
        remenu = np.array(text)
        #print('치환해서 출력: ', remenu)
        remenu = ' '.join(remenu)
        print(remenu)


###기존 rename파일에 합치기

#실험
import shutil

from_file_path = 'C:\Personal_prj\\rename.txt' # 복사할 파일
to_file_path = 'C:\Personal_prj\\copy_rename.txt' # 복사 위치 및 파일 이름 지정
shutil.copyfile(from_file_path, to_file_path) 

#계칸짐 자리에 들어가버리네..?
f = open('C:\Personal_prj\copy_rename.txt', 'r', encoding='utf-8')
f_out = open('C:\Personal_prj\copy_rename_.txt', 'w', encoding='utf-8')
while True:
    test = f.readline()
    if not test:
        break
    if correction_df.values.all() in test:
        for i in range(test.count(correction_df.values.all())):
            test = test.replace(correction_df.values.all(), remenu)
            f_out.write(test)
        print(test)

f_out.close()
f.close()

#가장 마지막 오타인 계칸짐 자리에 remenu(올바른 단어)전체 출력되어버림.//ㅠ