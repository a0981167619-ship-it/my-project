number=1000
'''
整數
'''
print(number)
number1=bin(number) 
print(number1)
number2=oct(number)
print(number2)
number3=hex(number)
print(number3)
x=int(number1,2)
print(x)
y=int(number2,8)
print(y)
z=int(number3,16)
print(z)

"""
浮點數
"""
xy=float.fromhex('0x56.Ep8')
print(xy)

yx=float.fromhex('0x7A.6p-8')
print(yx)

yz=float.hex(9.63)
print(yz)

zy=float.hex(888.0)
print(zy)

xyz=300.0
print(float.is_integer(xyz))

yxz=377.89895656787823565556689
print(float.is_integer(yxz))

zxy=7.156/7.895
print(round(zxy,10))

xzy=0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(round(xzy,15))

miy=3.65655*9.84211
print(round(miy,6))

kio=1.2+1.3
print(round(kio,1))
