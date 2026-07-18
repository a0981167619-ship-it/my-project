file=open('4.py','r',encoding='utf-8')#讀取此檔案內容
print(file.read())

file1=open('3-3 比較運算子.py','r',encoding='utf-8')
print(file1.read())

file2=open('button.py','rt',encoding='utf-8')#文本模式,搭配r使用
print(file2.read())

file3=open('5.py','tw+',encoding='utf-8')#搭配w+使用
file3.write('c=str(input("請輸入一個字串"))')
file3.seek(0)#回到開頭
harsh=file3.read()
print(harsh)

file4=open('78.empty.py','w')
file4.write('787878')
file4.write('joker is a evil character')

file5=open('78.empty.py','a')#用於追加此檔案內容
file5.write('Yes,I think so too.')

