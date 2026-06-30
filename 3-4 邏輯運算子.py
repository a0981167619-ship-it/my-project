x=2;y=10;z=13
result= x>y and y<z #and=[且]{∩} 必須兩者都成立才成立
print(result)
result= x>y or x<z #or=[或] {∪} 其中一個條件成立則成立
print(result)
result=not(result)#將原值轉變成相反的值
print(result)

"""[%] 格式化輸出
"""
a=588;b=60;c=3
print("a=%d,b=%d,c=%d"%(a,b,c))
print("::: 🧡 ━━━━━━━━━━━━━━ 🧡 :::::: 🧡 ━━━━━━━━━━━━━━ 🧡 :::")
print("a>b and a>c or a!=b=%d"%(a>b and a>c or a!=b))
print("a==b or a==c and a>b>c=%d"%(a==b or a==c and a>b>c))
print("not(a!=b) and not(a==b) or not(a>=b)=%d"%(not(a!=b) and not(a==b) or not(a>=b)))

"""
[format] 格式化輸出
"""
t=5
y=3
print(t,y)
print("• < ✨ ≫───•◦ ❈◦•───≪ ✨ > •")
print("{0}>={1} and {0}<={1}={s}".format(t,y,s="0"))
print("{0}!={1} or {0}=={1}={s}".format(t,y,s="1"))
print("not({0}<{1}) and not({0}!={1}) or not({0}=={1})={s}".format(t,y,s="1"))

k=1.235
b=1.732
if (k>=b and k!=b):
    print("False")
elif(k==b or k<=b):
    print("True")
elif(not(k>b) or not(k==b)):
    print("True")
else:
    print("False")

