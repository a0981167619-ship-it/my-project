x=int(input("請輸入一次數:"))
max=0
for i in range(1,x+1):
    print(">",end="")
    n=int(input("請輸入一整數:"))
if n<i:
    n=i
print("最大值為:%d"%(n))

