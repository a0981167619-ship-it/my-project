x=int(input("請輸入數值1:"))
y=int(input("請輸入數值2:"))
op=input("請輸入+-*/運算式:")

if op=="+":
    print("{}+{}={}".format(x,y,x+y))
elif op=="-":
    print("{}-{}={}".format(x,y,x-y))
elif op=="*":
    print("{}*{}={}".format(x,y,x*y))
elif op=="/":
    print("{}/{}={}".format(x,y,x/y))
else:
    print("運算子不符合")
    
