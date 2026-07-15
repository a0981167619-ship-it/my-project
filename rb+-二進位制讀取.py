file=open('rb+--ex.bin','wb')#建立二進位檔
file.write(b'123')#二進位制寫入
file.close()

file=open('rb+--ex.py','rb+')
print(file.read())#讀取內容ˊ

file.seek(1)#將游標移到索引值為1的位置
file.write(b'567889498958')

file.seek(0)

print(file.read())
file.close()

file1=open('1.bin','wb')
file1.write(b'right away')
file1.close()

file1=open('1.bin','rb+')
kity=file1.read()
print(kity)

file1.seek(10)
file1.write(b' prompt')
file1.seek(0)
print(file1.read())
file1.close()