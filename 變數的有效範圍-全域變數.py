def vague(x,y):
    z=25
    return x+y*z

x=85#全域變數
y=70#全域變數
print(vague(x,y))

def dim(a,b):
    score=15
    return a/b+score
scorek=56#全域變數
scorek1=100#全域變數
print("總分為:",dim(scorek,scorek1))#呼叫函數

def argument(n,m):
    total=156
    return n/m-total

a=158
b=205
print("總和為:",argument(a,b))
