file=open('範例檔--檔案組合模式.py','r+')#游標為檔案開頭
example=file.read()
print(example)

file.write('123456')#直接寫入此檔案
file.write('456789')
file.close()


