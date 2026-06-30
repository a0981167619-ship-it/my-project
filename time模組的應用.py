"""ex.1"""
import time
t=time.localtime()
t1=t.tm_wday
print("今天是星期幾:",t1)#2-為星期三
t=time.localtime()
print("現在是{0}點".format(t.tm_hour))

"""ex.2"""
print("start")
time.sleep(2)#時間暫停兩秒
print("end")
