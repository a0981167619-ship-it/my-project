list1=["curtail","detail","decline","decrease"]
list1.pop()#預設移除最後一個
print(list1)
list1.remove("detail")
print(list1)#串列中移除指定元素
list2=["increase","up to","add","minus"]
list2.pop(0)#移除第一個位置的元素
print(list2)
list2.remove("minus")
print(list2)

list3=[0.56,897,565,23,10,0.75896]
list3.sort()#將串列中的元素進行升冪排列(預設為False)
print(list3)
list3.reverse()#將串列中的元素反轉
print(list3)
list3.clear()#清空串列
print(list3)
list3.copy()#複製串列
print(list3)

list4=[0.00001,0.002,0.03,4,5,6,89,756]
list4.sort(reverse=True)#reverse=True進行降冪排列
print(list4)
list4.reverse()
print(list4)
list4.copy
print(list4)
list4.clear()
print(list4)

