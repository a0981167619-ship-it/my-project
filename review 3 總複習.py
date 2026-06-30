ideal=float.fromhex('0x5.Ap+1')
observe=float.fromhex('0xA.5p1')
print(int(ideal+observe))
print(int(ideal-observe))
print(int(ideal*observe))
print(int(ideal**observe)) #乘冪(次方)
print(int(ideal//observe)) #整數除法
print(int(ideal/observe))
print(int(ideal%observe))  #除法取餘數
"""
⚝與除法相關的運算子 第二個位元都不能為0 否則會發生除0錯誤(ZeroDivisonError)
"""
x=2
b=3
c=73
vit=x*b*b*c
f=str(vit)
fit=(x+b+b+x)
print(fit)
cat=(c-(x*b)-(x*b)-(x*b)-b)
print(cat)
k=(fit*cat)               #算術運算子
j=str(k)
print("LOVE:",j+f)
"""
3-2 複合指定運算子
"""
number=55.78
print(number)
number+=5
print(number)
number-=10
print(number)
number*=78
print(number) #移向概念
number/=70
print(number)
number//=45
print(number)
number**=0
print(number)
number%=8
print(number)

A=10
B=A+16
C=(A*B)%100
print("A=",A)
print("B=",B)
print("C=",C)
"""
3-3 比較運算子
"""
a=0.14285714;b=0.375
print("a>b=%d"%(a>b))
print("a<b=%d"%(a<b))
print("a>=b=%d"%(a>=b))
print("a<=b=%d"%(a<=b))
print("a==b=%d"%(a==b))
print("a!=b=%d"%(a!=b))

a=('0x5.4p+2')
b=('0xC.Dp10')
if (a>b):
    print("True") #if一旦成立,其他的皆不會執行
elif(a<b):
    print("False") 
elif(a>=b):
    print("1")
elif(a<=b):
    print("0")
elif(a==b):
    print("T")
else:
    print("F")

a=123
b=145
print("{}>{}={F}".format(a,b,F="False"))
print("{}=={}={F}".format(a,b,F="False"))
print("{}!={}={T}".format(a,b,T="True"))
print("{}>={}={F}".format(a,b,F="False"))
print("{}<={}={T}".format(a,b,T="True"))
print("{}<{}={T}".format(a,b,T="True"))

"""
3-4 邏輯運算子
"""
x=15;y=65
z=bin(x)
n=bin(y)
print(z , n)
print("🧡 .·:*¨ ¨*:·. 🧡🧡 .·:*¨ ¨*:·. 🧡🧡 .·:*¨ ¨*:·. 🧡🧡 .·:*¨ ¨*:·. 🧡🧡 .·:*¨ ¨*:·. 🧡🧡 .·:*¨ ¨*:·. 🧡")
print("z>n and z!=n or z==n=%d"%(z>n and z!=n or z==n))
print("z!=n or (not z<=n) and z==n=%d"%(z!=n or (not z<=n) and z==n))

c=oct(789)
b=oct(456)
print(c , b)
if (c>b):
    print("True")
elif(c==b):
    print("False")
elif(c<=b):
    print("0")
elif(c>=b):
    print("1")
elif(c!=b):
    print("T")
else:
    print("F")
"""
3-5 運算子的優先權
"""
"""Q1. 老闆買進 25 桶油漆，每一桶油漆的重量都是 5.345 公斤。
請問 25 桶油漆總重量大約是多少公斤？(先用四捨五入法將油漆的重量
取概數到小數第一位後，再計算油漆的總重量)
1 132.5
2 133.6
3 135
4 132  """
x=5.345
y=print(round(x,1))
z=(5.3*25)
print("油漆總重量為:",z) #Ans:1

"""
Q2. 一盒彩色筆 175 元，一枝水彩筆 25 元，買 8
盒彩色筆和 8 枝水彩筆共要多少元？
"""
a=8*(175+25)
print("共要%d元"%a)

"""
Q3.請設計一程式分別請使用者輸入5科的分數 並計算平均
"""
math=input("請輸入數學的分數:")
m=float(math)
chinese=input("請輸入國文成績:")
c=float(chinese)
English=input("請輸入英文成績:")
E=float(English)
scient=input("請輸入自然成績:")
s=float(scient)
social=input("請輸入社會成績:")
S=float(social)
z=(m+c+E+s+S)//5
print("5科平均為:%1.2f"%(z))





 
