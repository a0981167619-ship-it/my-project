"""15.動態規劃法+遞迴(每塊可拼1、2塊)"""
def square(n):
    if n==0:
        return 1
    if n<0:
        return 0
    else:
        return square(n-1)+square(n-2)
print(square(7))

"""動態規劃法"""
n=7
square=[0]*(n+1)
square[0]=1
square[1]=1
for i in range(2,n+1):
    square[i]=square[i-1]+square[i-2]
print(square[n])

"""拼糖果塔(1、3、4種)"""
def candy(n):
    if n==0:
        return 1
    if n<0:
        return 0
    else:
        return candy(n-1)+candy(n-3)+candy(n-4)
print(candy(12))

"""動態規劃法"""
n=12
candy=[0]*(n+1)
candy[0]=1
candy[1]=1
for i in range(2,n+1):
    candy[i]=candy[i-1]+candy[i-4]+candy[i-3]
print(candy[n])