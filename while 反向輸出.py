x=int(input("請輸入一數字:"))
while x!=0:
    print("反向輸出為",end="")
    print("%d"%(x%10))
    x//=10

y=int(input("請輸入一數字:"))
v=float(input("請輸入一數字:"))
while y!=0:
    print("%d*%f=%d"%(y,v,y*v))
    y=0
      

