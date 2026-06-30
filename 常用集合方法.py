x=set("1,2,3,4,5")
x.add("6")#新增集合元素
print(x)
y=x.copy()#複製集合
print(y)
z=x.clear()#清空集合
print(z)

X=set("1,2,3,6,7,8,9,10")
X.add("%")
print(X)
Y=X.copy()
print(Y)
Z=X.clear()
print(Z)

"""difference()的使用"""
a=set("1,18,56,23,45")
b=set("1,23,45,99,786")
c=a.difference(b)#取兩集合的差集
print(c)

"""discard(item)/remove(item)的使用"""
secure={"safe","dangerous",6}
loyal=secure.discard("dangerous")#移除一個集合中的元素
print(loyal)
disloyal=secure.remove(6)#移除集合中的一個元素
print(disloyal)

s={"O","R","D","I","N","A","R","Y"}
l=s.discard("O")
print(l)
d=s.remove("Y")
print(d)