import time
'''struct_time'''
year=time.localtime().tm_year
print('今年是{0}年'.format(year))
month=time.localtime().tm_mon
print('現在是%s月'%(month))
day=time.localtime().tm_mday
print('今天是{0}月{1}日'.format(month,day))
hour=time.localtime().tm_hour
print('現在是{0}點'.format(hour))
minute=time.localtime().tm_min
second=time.localtime().tm_sec
print('現在是{0}點{1}分{2}秒'.format(hour,minute,second))#為24小時制
week=time.localtime().tm_wday
print('今天是{0}'.format(week))###0代表星期一
days=time.localtime().tm_yday
print('今天是一年中的第%s天'%(days))

'''查看是否有夏令時'''
summertime=time.localtime().tm_isdst
print('是否有夏令時:',summertime)#預設為0,0為沒有,1為有
