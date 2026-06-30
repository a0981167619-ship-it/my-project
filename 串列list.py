list1=["1,23","fascinating","1.23"] #建立串列
print(list1)
list2=["awful","hideous","scorching"]
print(list2)
list3=["champion","chaotic","12345678910"]
print(list3)

list4=["3.14159","Java","filthy",False,2]#從2開始索引
print(list4[3])
list5=["c++","###",True,1]#從1開始索引
print(list5[2])

"""切片清單"""
print(list4[2:4:1])#從2開始索引,到4結束,每次跳一格
print(list5[0:3:2])#從0開始索引,到3結束,每次跳兩格

print(list1*9)
print(list2+list4)
print(list3*2)
print(list1+list2)