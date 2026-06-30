"""數值函數的使用"""
a=7.98
print(int(a))#將a四捨五入到整數
b=9991
print(bin(b))#取9991的二進位
c=4561
print(hex(c))#取4561的十六進位
d=1000
print(oct(d))#取1000的八進位
e=56
print(float(e))#把56換成浮點數
f=-3.987465
print(abs(f))#取-3.987465的絕對值
g=216
print(chr(216))#回傳216所對應的字元
"""ord()函數"""
h='A'
print(ord(h))#傳回'A'的unicode編碼
h1='Q'
print(ord(h1))#傳回'Q'的unicode編碼
h2='1'
print(ord(h2))#傳回'1'的unicode編碼

i=546
print(str(i))#將數值546轉為字串

"""數值函數綜合"""
a=-7.6
b=3.2
c=10
print('a的絕對值為:',abs(a))
faithful=abs(a)
explicit=faithful+b#將a的絕對值與b相加
print(explicit)

implicit=round(explicit,1)#使用round(),將結果四捨五入到小數點第一位
intelligent=max(implicit,c)
print('較大的數為:',intelligent)#使用max()比較,輸出較大的數
