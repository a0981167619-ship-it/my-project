"""round()函數"""
x=round(7.89,1)#取小數點後1位
print(x)
y=round(78.95,2)#取小數點兩位,前面為奇數,保留
print(y)
z=round(78.6)#四捨六入
print(z)

"""計算平均"""
a=87
b=92
c=76
d=(a+b+c)/3
d1=round(d)#四捨六入到整數
print("平均值為:",d1)