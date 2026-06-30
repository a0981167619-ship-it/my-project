N1=int(input("請輸入一整數:"))
N2=int(input("請輸入一整數:"))
if N1<N2:
    max=N1
    N1=N2
    max=N2
while N2!=0:
    N1,N2=N2,N1%N2
print("最大值為:%d" %N1)
