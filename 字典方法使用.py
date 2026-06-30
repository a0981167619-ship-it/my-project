"""清除-clear()"""
dict1={"num":100,"num1":200,"num3":300}
dict1.clear()#清空整個字典
print(dict1)
dict2={"fragile":"frail","weak":"delicate"}
dict2.clear()
print(dict2)

"""複製dict物件-copy()"""
dict3={"respond":"answer","motivate":"promote"}
dict4=dict3.copy()#dict4=dict3複製
print(dict4)
dict4["respond"]="question"#更改字典的key鍵
print(dict4)
print(dict3)#原字典內容將不會受影響

dict5={"unique":45,"common":7.896}
print(dict5)
dict6=dict5.copy()
print(dict6)

"""搜尋元素值-get()"""
a=dict3.get("respond")
print(a)
b=dict3.get("yield")#因沒有預設值,返回None
print(b)
c=dict3.get("yield",126)#返回預設值126
print(c)

d=dict5.get("unique")
print(d)
e=dict5.get("estimate",1.46533525665456465)
print(e)
f=dict5.get("estimate")
print(f)