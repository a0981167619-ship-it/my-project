K=float(input("請輸入初始溫度:"))
T=float(input("請輸入終溫:"))
n=float(input("請輸入物質的量:"))
U=float(input("請輸入實測內能變化:"))
R=8.314
theory=1.5*n*R*(T-K)
a=(U-theory)
print(a)

if (a<100):
    print("符合理論預測")
elif (100<=a<500):
    print("有誤差但可接受")
elif (a>=500):
    print("不符合熱力學預測")
else:
    print("False")

b=(T-K)

if (b<0):
    if (U>0):
        print("內能變化方向相反")
