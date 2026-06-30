"""14.動態規劃法(樓梯問題)、每次只能走1或2階"""
n=5
uin=[0]*(n+1)
uin[0]=1
uin[1]=1
for i in range(2,n+1):
    uin[i]=uin[i-1]#最後一步走一階
    if i>=2:
        uin[i]+=uin[i-2]
print(uin[n])#方法總數

"""每次只走1、3、5階"""
n=5
air=[0]*(n+1)
air[0]=1
air[1]=1
for i in range(2,n+1):
    air[i]=air[i-1]#最後一步走一階
    if i>=3:
        air[i]+=air[i-3]#最後一步走三階
    if i>=5:
        air[i]+=air[i-5]#最後一步走5階
print(air[n])

"""買飲料問題(2、4元)"""
n=10
drink=[0]*(n+1)
drink[0]=1
drink[1]=1
for i in range(2,n+1):
    drink[i]=drink[1]
    if i>=2 and 4:
        drink[i]=drink[i-2]+drink[i-4]
print(drink[n])

"""12公尺(1、3階)"""
n=12
ela=[0]*(n+1)
ela[0]=1
ela[1]=1
for i in range(2,n+1):
    ela[i]=ela[1]
    ela[i]=ela[i-1]+ela[i-3]
print(ela[n])
