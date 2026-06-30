"[%] 輸出比較運算子"
x=777;y=888
print("x=%d y=%d"%(x,y))
print("⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝⚝") #用星星當分隔線
print("x>y,比較值為%d"%(x>y))#以0,1當成真值(True),假值(False)
print("x<y,比較值為%d"%(x<y))
print("x==y,比較值為%d"%(x==y))
print("x!=y,比較值為%d"%(x!=y))
print("x>=y,比較值為%d"%(x>=y))
print("x<=y,比較值為%d"%(x<=y))

a=56;b=38
print("{0}>{1}={true}".format(a,b,a>b,true="True"))
print("{0}<{1}={false}".format(a,b,a<b,false="False"))
print("{0}=={1}={false}".format(a,b,a==b,false="False"))
print("{0}!={1}={true}".format(a,b,a!=b,true="True"))
print("{0}>={1}={true}".format(a,b,a>=b,true="True"))
print("{0}<={1}={false}".format(a,b,a<=b,false="False"))

i=-3.162;j=3.0
if (i>j):
    print("True")
elif(i<j):
    print("False")
elif(i==j):
    print("False")
elif(i!=j):
    print("True")
elif(i>=j):
    print("True")
else:
    print("False") #(i<=j)


