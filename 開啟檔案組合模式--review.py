file=open('檔案組合模式--範例檔.py','r+')#用於寫入
file.write('tuple=(1,2,3,4,5)')
file.seek(0)
print(file.read())

file1=open('檔案組合模式--範例檔.py','w+')#會清空原檔案中的內容
file1.write('list=[1,2,3,4,5]')
file1.seek(0)
print(file1.read())

file2=open('檔案組合模式--範例檔.py','a+')
print(file2.read())#讀取檔案中原本的內容
file2.write('\na=5\nb=6\n')
file2.seek(0)
print(file2.read())
file2.write('print(a/b)')
file2.seek(0)
print(file2.read())