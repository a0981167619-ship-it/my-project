with open('元組練習.py','r',encoding='utf-8') as file:
    a=file.read()
    print(a)#讀取此檔案裡的內容

try:
    file1=open('參數預設值.py','r',encoding='utf-8')
finally:
    b=file1.read()
    print(b)

with open('with -as--範例檔.py','w+') as j:
    j.write('I was enchant to meet you.')
    j.seek(0)
    print(j.read())
    
try:
    file=open('with -as--範例檔.py','w+')
finally:
    file.write('me too.')
    file.seek(0)
    finish=file.read()
    print(file.read())
    file.close()