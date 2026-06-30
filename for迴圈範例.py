"""請使用for迴圈設計一程式,可輸入小於100的整數n 並計算1*1+2*2+3*3+4*4+...+(n-1)*(n-1)+n*n"""

total=0
n=int(input("請輸入一整數:"))
if n>=1 or n<=100:
      for i in range(n+1):
          total+=i*i
          print("1*1+2*2+3*3+...%d*%d=%d"%(n,n,total))
"""99乘法表"""
for i in range(1,10):
    for o in range(1,10):
        print("{0}*{1}={2:^5}".format(i,o,i*o))
        print()
"""利用巢狀for迴圈來設計一程式,輸入n,求出1!+2!+...n的和"""
total=0
n1=1
n=int(input("請輸入一個整數:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        n1*=j #計算n!的值
        total+=n #計算1!+2!+...的值
        print("1!+2!+...%d!=%d"%(n,total))
