import datetime
civilized=datetime.date.today()#取得今天日期
print(civilized)

domestic=datetime.datetime.now()#取得現在時間
print(domestic)

tender=datetime.date(2026,7,8).weekday()#取得星期數,0-星期一,6-星期天
print(tender)
rough=datetime.date(2026,2,5).weekday()
print(rough)

tough=datetime.date(2026,7,8).isoweekday()#取得星期數,0-星期一,7-星期天
print(tough)
scarce=datetime.date(2026,2,5).isoweekday()
print(scarce)

"""datetime.date.isocalendar()方法"""
dense=datetime.date(2028,4,5).isocalendar()#返回年、週數、星期數
print(dense)
sparse=datetime.date(2030,9,24).isocalendar()
print(sparse)