file=open('wb+-ex.bin','wb+')
file.write(b'kilo mega tera')#使用二進位制寫入
file.seek(0)
a=file.read()
print(a)

file.seek(10)#將游標移到索引值為15的位置
file.write(b'milli giga femto')
b=file.read()
print(b)
file.close()