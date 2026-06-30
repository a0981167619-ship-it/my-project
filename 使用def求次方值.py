""""求取某數次方值"""
def raw(x,y):
    for i in range(y+1):
        x**=y
        return x
x=int(input("請輸入x值:"))
y=int(input("請輸入y值:"))
print("次方值為:%d"%raw(x,y))#呼叫函數

"""判斷奇數、偶數"""
def num(x):
    if x%2==0:
        return("此數為偶數")
    else:
        return("此數為奇數")
x=int(input("請輸入X值:"))
print("此數為:%s"%num(x))
