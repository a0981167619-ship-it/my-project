import time
t=time.strftime('%S',time.localtime())
print('秒為:',t)

t=time.strftime("%U",time.localtime())
print("一年中的星期數:",t)#以星期天是一個星期的開始

t=time.strftime('%w',time.localtime())
print('一個星期中的第幾天:',t)#以0當星期天

t=time.strftime('%W',time.localtime())
print('一個星期中的第幾天',t)#以星期一為一個星期的開始

t=time.strftime('%x',time.localtime())
print('本地相應日期:',t)

t=time.strftime('%X',time.localtime())
print("本地相應時間:",t)

t=time.strftime('%y',time.localtime())
print("去掉世紀的年份為:",t)

t=time.strftime("%Y",time.localtime())
print("四位數的西元年為:",t)

t=time.strftime("%Z",time.localtime())
print("時區的名稱為:",t)

t=time.strftime('%%',time.localtime())
print("字元為:",t)