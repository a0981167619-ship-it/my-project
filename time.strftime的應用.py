import time 
t=time.strftime('%Y-%m-%x-%M-%S',time.localtime())
print(t)

"""基礎顯示"""
t=time.strftime("%c",time.localtime())
print("現在時間為:",t)

"""日誌紀錄"""
t=time.strftime("%Y-%m-%d",time.localtime())
print("今天日期為:",t)
