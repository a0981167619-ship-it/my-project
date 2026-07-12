"""請設計一程式決定星期三才要穿藍色衣服,而星期四穿白色T恤的程式"""
X=input("請輸入3或4:") #3或4代表星期三或星期四
y=int(X)
if y==3:
    print("穿藍色衣服")
if y==4:
    print("穿白色T恤")
'''
if 的單行敘述
'''
a=input("請輸入餘額:")
g=int(a)
if (g>200): print(">200元")

'''
if的多行敘述
'''
b=input("請輸入英文成績:")
score=int(b)
if (score>=60):
    print("Pass")
    print("great!")

