import time
t=time.strftime('%a',time.localtime())
print("本地簡化星期名稱為:",t)

t=time.strftime('%A',time.localtime())
print("本地完整星期名稱為:",t)

t=time.strftime('%b',time.localtime())
print("本地簡化月份名稱為:",t)

t=time.strftime('%B',time.localtime())
print('本地完整月份名稱為:',t)

t=time.strftime('%c',time.localtime())
print('本地相應日期和時間表示:',t)

t=time.strftime('%d',time.localtime())
print('一個月中的第幾天:',t)

t=time.strftime('%H',time.localtime())
print("一天中的第幾個小時:",t)#24小時制

t=time.strftime('%I',time.localtime())
print('第幾個小時:',t)#12小時制

t=time.strftime("%j",time.localtime())
print('一年中的第幾天:',t)

t=time.strftime("%m",time.localtime())
print("月份:",t)

t=time.strftime('%M',time.localtime())
print('分鐘數:',t)

t=time.strftime("%p",time.localtime())
print("本地am或者pm相應符",t)