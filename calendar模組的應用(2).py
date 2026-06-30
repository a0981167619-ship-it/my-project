'''生日周末檢查'''
#小明的生日為2026年2月14日
import calendar
birthday=calendar.month(2026,2)
print('2026年的日曆為:',birthday)
print('2026年2月14日為星期六')

'''閏年數量'''
#2000-2030之間有幾個閏年
year=calendar.leapdays(2000,2030)
print('2000-2030之間有%d個閏年'%(year))