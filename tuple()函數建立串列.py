tuple=list()#建立空串列
print(tuple)
tuple1=list([0.127,0.128,0.129,0.130])
print(tuple1)

"""取得元組中的元素與串列相同"""
tuple2=("Southern Hemisphere","***",23,1.25)
print("tuple2[3]:",tuple2[3])#取索引位置第三個
tuple3=("Arctic","Antarctic",2.03,4.015,5.677)
print("tuple3[0]:",tuple3[0])#取索引位置第0個

"""檢查某一元素是否存在於元組中"""
tuple4=("156",156,"ally","enemy",3.74)
a="enemy" in tuple4 #使用in與not in 檢查元素是否存在於元組中
print(a)
b="156" not in tuple4
print(b)
c=1.56 not in tuple4
print(c)

