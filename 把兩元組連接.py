"""使用+與*連接兩元組"""
tuple1=("draw lots",1,2,3,"guest")
tuple2=(1.56,7,89,10.08,9.12,3.56)
tuple3=(tuple1+tuple2)#使用+號連接兩元組
print(tuple3)
tuple4=(tuple2*3)#複製tuple4元組
print(tuple4)

tuple5="8","defeat","victory",5,6,9
tuple6=("10",)
print(tuple5+tuple6)
d=tuple6*10 #複製10個tuple6
print(d)
s="10" in d
print(s)
