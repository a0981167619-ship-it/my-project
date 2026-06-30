belt=input("請輸入腰圍:")
height=input("請輸入身高:")
X=float(belt)
Y=float(height)
x=(X/Y) #計算腰高比
print("腰高比為:"+str(x))

if(x<0.4):
    print("過瘦")
elif(0.4<x<0.49):
    print("健康範圍")
elif(0.50<x<0.59):
    print("風險偏高")
else:
    print("肥胖風險高")


