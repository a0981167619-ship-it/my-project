import time
t=time.perf_counter()#取得程式執行時間
print(t)

t=time.process_time()#取得程式執行時間
print(t)

t=time.process_time()
r=time.sleep(100)#程式暫停100秒
r=time.sleep(0.5)#程式暫停0.5秒
print(t)