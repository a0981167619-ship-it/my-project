import math
x=-99
print(math.fabs(x))#取x的絕對值,回傳浮點數
kill=-16384
print(math.fabs(kill))
mention=2.03
y=6
print(math.fmod(kill,mention))
print(math.fmod(x,y))#x除以y取餘數
print(math.pow(x,y))#x的y次方
print(math.pow(mention,y))

"""階乘"""
account=math.factorial(y)#y的階乘
print(account)
z=10
multiply=math.factorial(z)
print(multiply)#10的階乘

bury=0
print(math.isnan(bury))#bury若不是數字為True,是數字則為False
worries=56
print(math.isnan(worries))

print(math.gcd(y,worries))#取x與worries的最大公約數

harmony=199
kind=99
print(math.gcd(harmony,kind))#兩者的最大公因數為1

"""math模組的應用"""
#求價差
x=12.5
y=15.8
xy=12.5-15.8
print('兩禮物的價差為:',math.fabs(xy))

#求剩幾個氣球
zealous=50
z=7
print('還剩%d個氣球'%(math.fmod(zealous,z)))

a=10
d=2.25
print('第三層糖粉量:{0}'.format(math.pow(a,d)))

#求12的階乘
print('12的階乘為:',math.factorial(12))

s=48
print('48是有效數字嗎?',math.isnan(s))#不是有效數字

#求12與18的公因數
secret=12
hide=18
print('12與18的最大公約數為:',math.gcd(12,18))
