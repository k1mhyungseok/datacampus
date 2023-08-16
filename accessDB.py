import numpy as np
import pandas as pd
import os


# ingredient 변수의 원소값들을 str -> list로 변환
def preprocess_sublist(col_name, df):
    stopword = ["'", '[', ']', ' ']
    sub_list = []
    for i in df[col_name]:
        word = ''
        for k in i:
            if k not in stopword: word += k
        sub_list.append(word.split(sep=','))
    res = []
    for i in range(len(df)):
        if len(sub_list[i][0]) == 0:res.append(np.nan)
        else: res.append(sub_list[i])
    df[col_name] = res
    return None


### 사용법 df = accessDB.read_db(db_path)
### df에 db가 저장됨
def read_db(db_path):
    df = pd.read_csv(db_path, sep = '|', header = 0).iloc[:, 1:]
    col_list = df.columns[8:14].values
    for i in col_list: preprocess_sublist(i, df)
    return df

# 알러지 이미지 return 함수
def find_image(img_path, target):
    target_filename = '{}_image.jpg'.format(target)
    for root, dirs, files in os.walk(img_path):
        if target_filename in files:
            return os.path.join(root, target_filename)
    return print("There's No img in DB")


### 사용법 df_finder('음식명', '원하는 정보', db 저장한 객체명)
def db_finder(food_name, info, df):
    if info == '알러지ko': # 알러지 한국어.ver
        allergy_list = [y for x in df.loc[(df['ko'] == food_name)]['allergy.ko'] for y in x]
        allergy_data ={
            'image' : ["allergy_image/{}_image.jpg".format(x) for x in allergy_list],
            'description' : allergy_list #리스트
        }
        return allergy_data

    elif info == '알러지en': # 알러지 영어.ver
        allergy_list = [y for x in df.loc[(df['ko'] == food_name)]['allergy.ko'] for y in x]
        allergy_data ={
            'image' : ["allergy_image/{}_image.jpg".format(x) for x in allergy_list],
            'description' : [y for x in df.loc[(df['ko'] == food_name)]['allergy.en'] for y in x]
        }
        return allergy_data
        
    # elif info == 






    # if col == 'allergy':
    #     row = df[df['ko'] == ko] #여기서 df는 read_db로 정제된 df가 되어야 함
    #     allergy = row['allergy'].values[0] #리스트의 첫 str이 결과값으로 들어올 것 
    #     for i in allergy:
    #         display(Image(filename=find_image(image_path, i))) #이미지 display 필요 없으면 삭제
    #         find_image(image_path, i)
    
    # elif col == 'ingredient':
    #     # ingredient_app.py 수정 후 실행하는 코드

    # elif col == 'ko':
    #     # food_app.py 수정 후 실행하는 코드

# 알러지 사진 저장될 경로
# folder_name = r'C:\Users\take0\Desktop\kdata_db\식재료 이미지'
# if not os.path.exists(folder_name):
#     os.makedirs(folder_name)
# else:
#     for f in os.listdir(folder_name):
#         os.remove(os.path.join(folder_name, f))