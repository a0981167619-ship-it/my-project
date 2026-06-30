tuple1=(10,20,30,40,50,60,70,80,90,100)
print("元組元素個數為:",len(tuple1))#計算元組元素個數
print("元組元素中元素最大值為:",max(tuple1))#返回元組元素中元素最大值
print("元組元素中最小值為:",min(tuple1))#返回元組元素中最小值

list1=["maximum","minimum","minimal",230,343]
print(tuple(list1))#將串列轉換為元組
print(sum(tuple1))#加總元組內個元素總和

tuple2=(1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400)
print(len(tuple2))
print(max(tuple2))
print(min(tuple2))

list2=[441,484,529,576,625,676,729,784,841,900,961,1024]
print(tuple(list2))
print(sum(tuple2))