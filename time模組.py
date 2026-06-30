import time #匯入時間模組
"""查看原始時間"""
t=time.time()
print(t)
t=time.localtime()#把時間戳變成當前的時區
print(t)

t=time.localtime()
print(t.tm_year)#輸出年
print(t.tm_mon)#輸出月
print(t.tm_mday)#輸出日
print(t.tm_hour)#輸出當前時間
print(t.tm_min)#輸出當前分
print(t.tm_sec)#輸出當前秒
print(t.tm_wday)#輸出weekday(0-星期一)
print(t.tm_yday)#一年中的第幾天
print(t.tm_isdst)#是否為夏令時(0-無使用夏令時,1-有使用夏令時)

"""struct_time變為時間戳"""
t=time.mktime(time.localtime())#把struct_time變為秒數
print(t)

"""time.asctime"""
t=time.asctime()#struct_time變字串
print(t)

"""time.ctime"""
t=time.ctime()
print(t)
t=time.ctime(time.time())
print(t)
t=time.ctime(12578905)#把一個時間戳轉換為類似'Wed Feb 4 10:58:09 2026'的形式
print(t)
