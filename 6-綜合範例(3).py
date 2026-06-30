"""1.帳號與Gmail檢查"""
a=str(input("請輸入使用者名稱:"))
b=str(input("請輸入Gmail:"))
while b.endswith("gmail.com")==False:
    c=str(input("請重新輸入Gmail:"))
if b.endswith("gmail.com")==True:
    print(b)
    print(a)
"""2.標題美化(字串處理)"""
d=str(input("請輸入一個標題文字:"))
e=str(input("是否要自訂前後符號:(Y/N):"))
if e=="Y":
    f=str(input("請輸入符號:"))
    g=f.center(30,str(f))
    print(g)
    if e=="N":
        h=d.center(30,"-")
print(d)
