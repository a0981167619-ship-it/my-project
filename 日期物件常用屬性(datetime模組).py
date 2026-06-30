import datetime
x=datetime.date.min #取得支援最小日期
print(x)
y=datetime.date.max #取得支援最大日期
print(y)
z=datetime.date(2026,12,31).year #取得年
print(z)
z1=datetime.date(2047,1,1).year
print(z1)

xy=datetime.date(2026,12,31).month #取得月
print(xy)
yx=datetime.date(2047,1,1).month
print(yx)

yz=datetime.date(2026,12,31).day #取得日
print(yz)
yz1=datetime.date(2047,1,1).day
print(yz1)