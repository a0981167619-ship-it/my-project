def function(a,b,c):
    x=(a+b)*c
    print(x)

print(function(12,36,58))#省略回傳return,輸出為None

"""數字比大小"""

def MAX(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("請輸入a值:"))
b=int(input("請輸入b值:"))
print("較大值為:%d"%MAX(a,b))#呼叫函數MAX

"""#數字比大小"""

def min(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
a=int(input("請輸入a值:"))
b=int(input("請輸入b值:"))
c=int(input("請輸入c值:"))
print("較小值為:%d"%min(a,b,c))