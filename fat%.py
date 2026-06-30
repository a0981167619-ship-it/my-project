a=str(input("請輸入性別:"))
b=float(input("請輸入身高:"))
c=float(input("請輸入體重:"))
d=int(input("請輸入年齡:"))
BMI=float(c/(b/100)**2)
print("BMI值:",BMI)

if str("a=女"):
   s=(1.20*BMI+0.23*d-5.4)
   print("體脂率:",s)
s=(1.20*BMI+0.23*d-5.4)
if (s<18):
    print("過低")
elif(18<=s<28):
    print("正常")
elif(s>28):
    print("過高")
    
   
elif str("a=男"):
     k=(1.20*BMI+0.23*16.2)
     print("體脂率:",k)
elif(2<=k<5):
    k=(1.20*BMI+0.23*16.2)
    print("必要脂肪")
elif(6<=k<13):
    print("運動員")
elif(14<=k<17):
    print("一般適中(健康)")
elif(18<=k<24):
    print("邊緣過高")
else:
    print("過高")

input("按enter結束鍵結束程式")
   
