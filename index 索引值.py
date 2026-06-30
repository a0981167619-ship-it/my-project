phase=["log1","log10","log100"]
for index,log in enumerate(phase):
    print("{0}✿✿{1}".format(index,log)) #索引phase
    
"""輸入<100 Z 計算1*1+2*2+3*3+4*4+...(n-1)*(n-1)+n*n"""
total=0
number=int(input("請輸入一整數:"))
if number>=1 or number<=100:
    for Y in range(number+1):
        total+=Y*Y
    print("1*1+2*2+3*3+4*4+...%d*%d=%d"%(number,number,total))
else:
    print("輸入數字超出範圍")
"""輸入一次數 用for迴圈控制數目 並且找出MAX"""
MAX=0
for K in range(10):
    print(">")
    uni=int(input("請輸入一數字:"))
    if MAX<uni:
        MAX=uni
        print("最大值為:%d"%(MAX))
"""100*100乘法表"""
for i in range(1,101):
    for k in range(1,101):
        print("{0}*{1}={2:^2}".format(i,k,i*k))
"""輸入ZN,求1!+2!+...n!的和"""
total=0
n0=1
n=int(input("請輸入一整數:"))
for i in range(1,n+1):
    for k in range(1,i+1):
        n0*=k #n!的值
    total+=n0
    n0=1
print("1!+2!+...%d!=%d"%(n0,total))
