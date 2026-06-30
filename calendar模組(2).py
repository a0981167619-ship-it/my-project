import calendar
tolerant=calendar.calendar(2026,w=1,l=2,c=2)#生成2026年的日曆
print('日曆為:',tolerant)
intolerant=calendar.calendar(1919,w=1,l=1,c=1)
print(intolerant)

journal=calendar.month(2026,2,w=1,l=1)#生成2026年二月的日曆
print('2026年二月的日曆為:',journal)
derive=calendar.month(1977,12,w=2,l=1)
print('1977年12月日曆為:',derive)

today=calendar.firstweekday()#返回當前每周起始日期,預設為0,星期一為0,星期日為6
print('每周起始日期為:',today)

settoday=calendar.setfirstweekday(calendar.TUESDAY)#星期二為1
today1=calendar.firstweekday()
print('每周起始日期為:',today1)

settodat2=calendar.setfirstweekday(calendar.SATURDAY)#星期六為5
today2=calendar.firstweekday()
print('當前起始日期為:',today2)

'''判斷是否為閏年,是為True 否為False'''
year=calendar.isleap(2026)
print('2026是否為閏年:',year)

year2=calendar.isleap(1875)
print('1875年是否為閏年:',year2)

'''取得年跟年之間的閏年總數'''
careful=calendar.leapdays(2010,2026)
print('2010-2026的閏年總數為:',careful)
careless=calendar.leapdays(1488,1565)
print('1488-1565年間的閏年總數為:',careless)

"""回傳串列資料"""
civilized=calendar.Calendar(firstweekday=5)
scared=civilized.monthdayscalendar(2023,4)
print(scared)

dense=civilized.monthdayscalendar(2026,7)
print(dense)

'''生成純本文日曆'''
Text=calendar.TextCalendar(firstweekday=4)#以星期五作為初始
print(Text.formatmonth(2026,9))
word=calendar.TextCalendar(firstweekday=6)#以星期天作為初始
print(word.formatmonth(1023,6))

'''生成HTML日曆'''
HT=calendar.HTMLCalendar(firstweekday=3)
print(HT.formatmonth(1945,3))
print(HT.formatmonth(2026,3))