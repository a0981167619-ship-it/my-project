print(list('petite'))#使用list函數將字串轉成串列
print(list("challenging"))

"""搭配for,range函數"""
list1=[i for i in range(1,20)]#取1-19
print(list1)
list2=[k*20 for k in range(1,9)]
print(list2)
list3=[i/1000 for i in range(1,100)]
print(list3)

"""切片slicing運算"""
list7=["K","L","M","N","O","F"]
print(list7[0:3])
print(list7[1:])
print(list7[2:5])

list5=[0.6,0.7,0.8,0.9,20,30,500]
print(list5[0:7])#全取
print(list5[4:])#從第四索引位置開始取