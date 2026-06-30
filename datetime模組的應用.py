import datetime 
"""取得指定日期的資訊"""
a=datetime.date.today()
print("今天日期是:",a)
b=datetime.datetime.now()
print("現在時間為:",b)
c=datetime.date(2026,2,5).isoweekday()
print("今天是星期:",c)

"""上課提醒"""
X=datetime.datetime.now()
print("現在時間為:",X)
a=datetime.time(11,24,10).hour
if a<8:
    print("還沒到上課時間")
else:
    print("遲到了")

