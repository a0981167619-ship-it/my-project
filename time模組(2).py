import time
"""格式化字串"""
year=time.strftime('%y')
print('年份為:',year)#取得兩位數的年份
Year=time.strftime('%Y')
print('今年為:',Year)#取得四位數的年份
month=time.strftime('%m')
print('現在為%s月'%(month))#取得月份
day=time.strftime('%d')#取得月分中的天數
print('現在是{0}日'.format(day))
hour=time.strftime('%H')
print('現在為%s點'%(hour))#24小時制
Hour=time.strftime('%I')
print('現在為%s點'%(Hour))#12小時制
minute=time.strftime('%M')
print('現在為{0}分'.format(minute))#取得現在的分鐘
second=time.strftime('%S')
print('現在為%s秒'%(second))

'''簡化/完整星期名稱'''
week=time.strftime('%a')#簡化星期名稱
print('現在為{0}'.format(week))
Week=time.strftime('%A')#完整星期名稱
print('現在為{0}'.format(Week))

'''簡化/完整月份名稱'''
month=time.strftime('%b')
print('現在為{0}'.format(month))#簡化月份名稱
Month=time.strftime('%B')#完整月份名稱
print('現在為{0}'.format(Month))

'''一年中的星期數,以星期天為一星期的開始'''
weekend=time.strftime('%U')
print('是一年中的第%s星期'%(weekend))
'''一年中的星期數,以星期一為一星期的開始'''
Weekend=time.strftime('%W')
print('是一年中的{0}星期'.format(Weekend))

'''星期天為一星期的開始-%w'''
weekk=time.strftime('%w')
print('今天是星期%s'%(weekk))

