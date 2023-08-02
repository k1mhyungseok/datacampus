from PIL import Image
from PIL import ImageDraw
import os
import cv2 as cv
import easyocr
import numpy as np
import pandas as pd

# trycount = input("how many?")

# print("count is + " + trycount)

# for num in range(int(trycount)):
#     print("Hello {0}".format(num))


# img = Image.open('zzangnan.jpg')
# img.show()

#path = 업로드 이미지 경로
#while(path):
#   easyocr 모델
#   텍스트 인식 끝났으면 break

# def main():
#     # 이미지 읽기
#     lena_color = cv.imread("ex_img.png", cv.IMREAD_COLOR)
#     lena_gray = cv.imread("ex_img.png", cv.IMREAD_GRAYSCALE)
    
#     # 이미지 출력하기
#     cv.imshow("Title_color", lena_color)
#     cv.imshow("Tilte_gray", lena_gray)

#     # size 확인, 픽셀값 읽기
#     print("Size of Img\n", lena_color.shape)
#     print("Pixel value of (10,10)\n", lena_color[10,10])

# if __name__ == "__main__":
#     main()

#절대경로
# pth = os.getcwd()
# print(os.path.abspath(pth))

# #PATH의 기본 이름 반환
# PATH = r'C:/team2_prj/ex_img.png'
# print(os.path.basename(PATH))

# route = r'C:/team2_prj/ex_img.png'
    


# while(1):
#     img = int(input('숫자를 입력하세요: '))
#     print(img, "가 입력되었습니다")
#     answer = input('계속 하겠습니까? (y or n 입력): ')

#     if answer == 'n':
#         break
#     elif answer != 'n' or 'y':
#         print("다시 입력하세요")
#         answer = input('계속 하겠습니까? (y or n 입력): ')

# while(1):
#     route = r'C:/team2_prj/ex_img.png'
#     # img = Image.open(route)
#     # img.show()

#     reader = easyocr.Reader(['ko'], gpu=False)
#     result = reader.readtext(route)
#     print(result)

#     if result == True:
#         break

# i=0
# while(i<2):
#     reader = easyocr.Reader(['ko'], gpu=False)
#      esult = reader.readtext('C:\/team2_prj\ex_img.png')
#     result2 = reader.readtext('C:\/team2_prj\ex_img.png', detail=0)
#     print(result)
#     print(result2)

#     df = pd.DataFrame(result)
#     print(df)

#     df2 = pd.DataFrame(result2)
#     print(df2)
#     i += 1

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