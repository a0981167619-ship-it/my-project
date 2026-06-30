import calendar
dim=calendar.month(2026,2)#輸出2026年2月的日曆
print(dim)

manufacture=int(input("請輸入年份:"))
market=calendar.isleap(manufacture)#判斷是否為閏年
print(market)