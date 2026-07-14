file=open('w+-ex.py','w+')
finish=file.write('banana')
file.seek(0)#回到開頭
t=file.read()#查看寫入的內容
print(t)
file.close()

file1=open('w+-ex2.py','w+')
file1.write('Canada is my favorite country.')
file1.seek(0)
reading=file1.read()
print(reading)
file1.close()
