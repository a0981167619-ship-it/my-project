file=open('continue4.py','r',encoding='utf-8')
print(file.name)#取得檔案名稱

file1=open('12--file-example.py','w+')
file1.write('I want sleep.')
file1.writelines('\nLet it go.')#換行
file1.seek(0)#回到開頭
print(file1.read())

print(file.readline())#讀取檔案的整行字串

file2=open('dictionary.py','r',encoding='utf-8')

print(file2.readlines())#讀取結果以序列結構返回
print(file2.readline())