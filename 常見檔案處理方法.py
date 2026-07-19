file=open('example--file.py','w+')
file.write('entry system.\n')
file.flush()
file.write('check information.')
file.seek(0)
print(file.read())
print('當前位置為:',file.tell())#返回當前游標位置

file.truncate(25)#從字節25的地方開始切斷
file.seek(0)
print('當前文字內容為:',file.read())
file.truncate(5)#從字節5的地方開始切斷
file.seek(0)
print('當前文字內容為:',file.read())