list1=["youthful","✿","✧","100"]#len(list1)==4,從0開始索引
list1[len(list1)-2]="KLMNO"#replace list1[2]
print(list1)
list2=["pitch-black",True,False,"☀","45","67"]#len(list2)==6
list2[len(list2)-1]="$$$$$$"#replace list2[5]
print(list2)
list2[1]="black"
print(list2)
list1[3]=100000000000
print(list1)

del list1[1] #刪除list1第2索引位置
print(list1)
del list1[0]
print(list1)
del list2[5]
print(list2)