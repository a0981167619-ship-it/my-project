x=7.815;y=3.162
print("x>y,比較結果值為:%s"%(x>y))
print("x<y,比較結果值為:%s"%(x<y))
print("x==y,比較結果值為:%s"%(x==y)) #直接用真(True),假(False)做判斷
print("x!=y,比較結果值為:%s"%(x!=y))
print("x>=y,比較結果值為:%s"%(x>=y))
print("x<=y,比較結果值為:%s"%(x<=y))

"""
format輸出 人工判斷
"""
xy=4.56;yz=10.28
print("{}>{}={false}".format(xy,yz,false="0"))
print("{}<{}={true}".format(xy,yz,true="1"))
print("{}=={}={false}".format(xy,yz,false="0"))
print("{}>={}={false}".format(xy,yz,false="0")) #用0,1當真假值
print("{}<={}={true}".format(xy,yz,true="1"))
print("{}!={}={true}".format(xy,yz,true="1"))

a=float.fromhex('0xA.3p+2')
b=float.fromhex('0xF.Dp+10') #浮點數16進位判斷大小值

if (a>b):
    print("True")
elif(a<b):
    print("True")
elif(a==b):
    print("False")
elif(a!=b):
    print("True")
elif(a>=b):
    print("False")
else:
    print("True")
