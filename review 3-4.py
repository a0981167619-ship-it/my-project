a=float.hex(5.0)
b=float.hex(156.23) #以字串回傳16位數[進位]的浮點數
c=float.hex(999.100)
print("a=%s   b=%s    c=%s"%(a,b,c))
print("• < ✨ ≫───•◦ ❈◦•───≪ ✨ > •★　　★°★ . *. °☆ . ● . ★　☆　★ ° ☆ ¸. ¸★")
print("a>=b and a<c or a!=c=%s"%(a>=b and a<c or a!=c))
print("not(a==b) and not(a>c) or not(a>b<=c)=%s"%(not(a==b) and not(a>c) or not(a>b<=c)))

x=125
X=oct(x)
y=3789
Y=oct(y)
z=5566
Z=oct(z)
if (X<Y):
    print("1")
elif(X!=Z):
    print("0")
else:
    print("1")

j=float.fromhex('0x3.Ap+1')
h=float.fromhex('0x5.Fp3') #把16進位的浮點數轉成10進位
k=float.fromhex('0xB.3p10')
print("j=%s  h=%s  k=%s"%(j,h,k))
print("🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 🌸 ")
print("j>=k and k<=h or h==j=%d"%(j>=k and k<=h or h==j))
print("j!=k or j<=k (not k<=h)=%d"%(j!=k or j<=k  (not k<=h)))



