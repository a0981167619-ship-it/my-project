"""建立集合"""
a={"humble","arrogant","modest","proud"}#用大括號建立集合,無value值
print(a)
b={1,23,4,46}
print(b)

#以set()建立集合
c=set("humble")
print(c)
d=set(("humbel",))#單一元素仍可用此寫法
print(d)

e=set()
print(e)#建立空集合以set()建立

"""set()建立集合,括號裡只能有一個迭代物件"""
str1=set("vulnerable")
print(str1)
list1=set(["Earth","sun","Mars"])
print(list1)
tuple1=set((1,56,111,166))
print(tuple1)
dict1=set({"prosperous":1000000,"rich":35145535454,"wealthy":90000000})#使用dict當引數時,只會保留key
print(dict1)

list2=set(["moreover","furthermore","besides"])
print(list2)
str2=set("K")
print(str2)
dict2=set({"ocean":7,"sea":3,"beach":1})
print(dict2)
tuple2=set((3.78,1.78,-1.78))
print(tuple2)