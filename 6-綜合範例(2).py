"""4.利用集合方法印出出現在任一組樂透清單的數字、兩組都出現的數字、列出沒有出現在任一組樂透清單的數字"""
number={1,2,3,4,5,6,7,8,9,10,11,12}
print(number)
num1={3,5,7,10,12}
print("第一組樂透:",num1)
num2={2,5,6,11,12}
print("第二組樂透:",num2)

g=num2.intersection(num1)
print("有2個數字出現在其中一次開獎:",g)#取num1與num2的聯集

f=num2.union(num1)
print("有8個數字出現在其中一次開獎:",f)

q=number.symmetric_difference(num2)#number2與number取對稱差,輸出
p1=number.symmetric_difference(num1)
print(q)
print(p1)

q1={1,3,4,7,8,9,10}
p2={1,2,4,6,8,9,11}

d=q1.intersection(p2)
print("總共有4個不幸運數字:",d)