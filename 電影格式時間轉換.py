#2026-02-21 18:30:00
import time
'''轉成時間元組'''
a=time.strftime('2026-02-21 18:30:00')
print('轉成時間元組:',a)

'''轉換成時間形式'''
b=time.asctime()
print('本地時間描述為:',b)

c=time.strptime('2026/2/21/18/30/00','%Y/%m/%d/%H/%M/%S')
print('轉換為time.strptime型式:',c)

d=time.strftime('%d-%m-%Y')
print('strftime格式化時間為:',d)