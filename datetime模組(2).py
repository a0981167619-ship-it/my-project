import datetime
daily=datetime.date(2026,2,19)
print('日期為:',daily)#日期類別
x=datetime.date(2027,4,18)
print('日期為:',x)

dazzle=datetime.time(hour=1,minute=5,second=36,microsecond=999)#時間類別
print('時間為:',dazzle)
y=datetime.time(13,14,5,4566)
print('時間為:',y)

dizzy=datetime.datetime(2026,2,19,1,5,36,999)#日期時間類別
print('日期與時間為:',dizzy)
z=datetime.datetime(2027,4,18,1,14,5,4566)
print('日期與時間為:',z)

delta=datetime.timedelta(weeks=2,days=3,hours=5,minutes=56,seconds=8,microseconds=6540,milliseconds=744)#時間間隔
print('時間差為:',delta)

time1=datetime.datetime(2026,7,8,5,40,10)
time2=datetime.datetime(2026,5,6,4,12,59)
diff=time1-time2#屬於datetime.timedelta的一部分
print('時間間隔為:',diff)
