tuple1=("Northern Hemisphere",1,5.0)#建立元組,以小括號表示
print(type(tuple1))
tuple2="Northern Hemisphere",1,5.0#也可以不以小括號表示
print(type(tuple2))

tuple3=("589")
print(type(tuple3))#不加逗點則被歸列為字串型態str()
tuple3=("589",)
print(type(tuple3))#加上逗點被視為元組型態

tuple4=(0.125,)
print(type(tuple4))