a="despair"
print(tuple(a))#將字串轉成元組
b="115220"
print(tuple(b))

"""將串列轉成元組"""
list1=["surprise","surprised","surprising","amaze","amazing"]
print(tuple(list1))

"""二維串列轉成元組"""

x=[[1,2],[3,4]]#建立二維串列
#二維串列轉成二維元組
y=tuple(map(tuple,x))
print(y)

"for寫法"
ATP=[[1,2],[3,4]]
ADP=[]
for i in ATP:
    ADP.append(tuple(i))
ADP=tuple(ADP)
print(ADP)

q=[['convex','concave'],['resist','yield'],['oppose','celsius','Fahrenheit']]
s=tuple(map(tuple,q))
print(s)

k=[['convex','concave'],['resist','yield'],['oppose','celsius','Fahrenheit']]
n=[]
for j in k:
    n.append(tuple(j))
n=tuple(n)
print(n)

