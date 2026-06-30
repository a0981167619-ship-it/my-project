Class={"group1","group2","group3","group4"}
class2={"group7","group5","group3","group4"}
a=Class.intersection(class2)#取兩者的交集
print(a)

b=Class.isdisjoint(class2)#判斷兩個集合是否包含相同的元素,沒有傳回True,有則傳回False
print(b)

c=Class.issubset(class2)#判斷集合的所有元素是否接包含在指定的集合中,是為True,否為False
print(c)

d=Class.issuperset(class2)##判斷集合的所有元素是否接包含原集合內,是為True,否為False
print(d)

e=Class.pop()#隨機移除一個元素
print(e)

f=class2.symmetric_difference(Class)#傳回兩個元素不同時存在的集合
print(f)

g=class2.union(Class)#取兩集合的聯集,重複的元素只會出現一次
print(g)

h=Class.update("group5")#修改當前集合,可新增元素
print(h)

num={0.89,0.61,0.23,0.78}
num1={0.89,0.78,5.06,1.23,0.23}

i=num.intersection(num1)
print(i)

j=num.isdisjoint(num1)
print(j)

k=num.issubset(num1)
print(k)

l=num.issuperset(num1)
print(i)

m=num1.pop()
print(m)

n=num.symmetric_difference(num1)
print(n)

o=num.union(num1)
print(o)

p=num.update("1.89")
print(p)