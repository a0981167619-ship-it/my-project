x,y=1,10
while x<y:
    x+=2
    print(x)
x,y=1,99
while y>x:
    y-=12
    print(y)
"""請設計一程式,利用while迴圈來求出使用者所輸入整數的所有因數"""
number=1
x=int(input("請輸入一整數:"))
print("%d的因數為:"%x)
while number<x:
    if x%number==0:
       print("%d為%d的因數"%(number,x))
       number+=1
"""請設計一程式,輸入一正整數n,利用while迴圈印出所有<=n的偶數"""
o=2
y=int(input("請輸入一偶數:"))
while o<y:
    if y%2==0:
        print("%d的所有偶數為%d:"%(y,o))
        o+=2
