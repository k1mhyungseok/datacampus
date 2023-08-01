import easyocr

reader = easyocr.Reader(['ko', 'en'], gpu=False)
result = reader.readtext('prac.jpg')

print(result)
print("hello")