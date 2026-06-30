"""5.帳號長度+格式檢查"""
x=str(input("請輸入帳號:"))
while len(str(x))<=6:
    y=str(input("請重新輸入帳號:"))
    if len(str(x))>=6:
       print("帳號設定完成:",x)
"""6.文字框線製作器"""
submissive=str(input("請輸入一串文字:"))
h=str(input("是否要制定框線符號(Y/N):"))
if h=="Y":
    l=str(input("請輸入一個符號:"))
    k=submissive.center(40,str(l))
    print(k)
    if h=="N":
        k1=submissive.center(40,"#")
        print(k1)

