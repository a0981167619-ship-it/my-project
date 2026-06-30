"""9.判斷是星期幾(數字)"""
import datetime
a=datetime.date(2026,2,11).weekday()
print(a)#以星期一為0,輸出2
b=datetime.date(2025,12,25).weekday()
print(b)

"""10.取得現在月份"""
a=datetime.datetime.now()
print("月份為:",a.month)

"""取得現在幾點"""
c=datetime.datetime.now()
print("現在為%d時"%(c.hour))

"""11.演算法-遞迴-分治法(計算整數n的冪次)"""
def f(n):
    a=int(input("請輸入一個整數:"))
    b=a**n
    if n==0:
        return 1
    else:
        c=a*a**(n-1)
        return c
print(f(5))
print(f(4))

"""12.演算法-遞迴-分治法(奇數總和)"""
def function(n):
    if n%2!=0:
        if n==1:
            return 1
        else:
            return n+function(n-2)
print(function(5))
print(function(9))

"""13.演算法-遞迴-最大公因數的分治法"""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(48,18))
print(gcd(56,98))
print(gcd(7,13))
   
    
    
        
    
    

