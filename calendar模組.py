import calendar #匯入模組
c=calendar.weekday(2026,2,4)
print(c)#回傳值為2,為星期三
d=calendar.weekday(2026,2,2)
print(d)#回傳值為0,為星期一

"""calendar.calendar(year)方法"""
print(calendar.calendar(2026))#傳回2026年的日曆
stable=(calendar.calendar(1945))
print(stable)

"""calendar.isleap(year)函數"""
unstable=calendar.isleap(2026)
print(unstable)#判斷是否為閏年
elaborate=calendar.isleap(1958)
print(elaborate)

"""取得某一指定月份的日曆"""
crude=calendar.month(2026,2)
print(crude)
refined=calendar.month(1458,12)
print(refined)

"""設定日曆的第一天"""
calendar.setfirstweekday(calendar.MONDAY)#設定日曆的第一天
raw=calendar.month(2026,2)
print(raw)

calendar.setfirstweekday(calendar.THURSDAY)
cooked=calendar.month(2025,7)
print(cooked)