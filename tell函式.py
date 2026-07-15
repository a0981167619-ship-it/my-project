file=open('tell範例檔.py','w+')
say=file.tell()
print('目前游標位置:',say)#顯示目前游標所在位置

file.write('If I fall in with you')
say2=file.tell()
print('目前游標位置:',say2)#得到文字寫入後的游標位置

file.write("but I don't like you")
print('目前游標位置:',file.tell())
file.seek(15)#將游標移到15的位置
print('目前游標位置:',file.tell())