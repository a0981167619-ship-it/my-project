'''運動計畫'''
import datetime
a=datetime.date(2026,2,19)
print('今天日期為:',a)
b=datetime.time(3,20)
print('放學時間為:',b)

d1=datetime.timedelta(hours=3,minutes=20)
c=datetime.timedelta(minutes=20)
d=datetime.timedelta(minutes=25)
e=datetime.timedelta(minutes=30)
print('籃球節目開始時間為:',d1+c+d+e)

beautiful=datetime.timedelta(minutes=50)
ability=datetime.timedelta(minutes=59)
print('晚餐時間為:',d1+c+d+e+beautiful+ability)