import time
'''time.strftime()-時間字串'''
time1=time.strftime('%H')
time2=time.strftime('%M')
time3=time.strftime('%S')
print('現在為%s點-%s分-%s秒'%(time1,time2,time3))

year=time.strftime('%Y')
month=time.strftime('%m')
day=time.strftime('%d')
print('今年是{0}年-{1}月-{2}日'.format(year,month,day))

'''time.localtime/time.gmtime()'''
conherent=time.localtime()#轉換當前時區struct_time
print(conherent)

confusing=time.gmtime()#轉換當前的時區struct_time
print(confusing)

'''time.strptime()'''
dominant=time.strptime('2026/2/19','%Y/%m/%d')#把字串轉換為struct_time型別
print(dominant)
obedient=time.strptime('12:11:03','%H:%M:%S')
print(obedient)

"""time.asctime()"""
disobedient=time.localtime()
print(time.asctime(disobedient))#轉換成時間形式,#月份/日/時間/年
submissive=time.strptime('2025/2/3','%Y/%m/%d')
print(time.asctime(submissive))
