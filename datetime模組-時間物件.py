import datetime
faith=datetime.time.min #取得支援的最小時間
print(faith)

faithful=datetime.date.max #取得支援的最大時間
print(faithful)

fail=datetime.time(16,35,45).hour #取得時
print(fail)

fair=datetime.time(10,51,16).hour
print(fair)

failure=datetime.time(16,32,45).minute #取得分
print(failure)

unfair=datetime.time(10,52,3).minute
print(unfair)

unjust=datetime.time(16,35,45).second #取得秒
print(unjust)

just=datetime.time(10,53,40).second
print(just)

ill=(datetime.time(10,51,16, 321456).microsecond) #取得微秒
print(ill)

illness=(datetime.time(10,55,19, 2187).microsecond)
print(illness)