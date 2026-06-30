"""取得元組指定範圍內的元素"""
tuple1=(1,4,3)+(1,6,9)#把兩元組連接
print(tuple1)
tuple2=tuple1*9 #複製9個tuple1
print(tuple2)

tuple3=(128,256,512,1024,2048,4096)
print(tuple3[5])#取索引位置第5個元素
print(tuple3[-1])#負為由右至左取,取第一個元素
print(tuple3[0:3])#正為由左只右取,範圍為索引位置第0個到第3個位置
print(tuple3[-3:-1])#增減值step預設為1
print(tuple3[-2:-6])#因增減值設定為1,無法取得元素

tuple4=("synonym","antonym","optimism","pessimism","sorrow")
print(tuple4[1])
print(tuple4[-4])
print(tuple4[1:0])#無法取得元素
print(tuple4[0:4])
print(tuple4[-1:0])#無法取得元素,因索引位置沒有0

