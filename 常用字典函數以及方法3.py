"""dict.items()"""
dict1={"1":1,"2":2,"3":3,"4":4}
a=dict.items(dict1)#以列表包裹元組方式返回鍵值
print(a)
dict2={"conceal":71,"neglect":5,"ignore":841}
b=dict.items(dict2)
print(b)

"""dict.setdefault"""
dict3={"784":28}
d=dict3.setdefault("729")#無設定預設值,返回預設值None
print(d)
dict4={"729":27}
d1=dict4.setdefault("729")#返回預設值27
print(d1)

"""dict.update"""
dict5={"145":145,"149":149}
dict6={"149":150,"151":151}
c=dict5.update(dict6)#將字典中的key:value更新到另一字典中
print(dict5)

f=dict2.update(dict1)
print(dict2)

"""dict.pop"""
dict6={"Hank":0.001,"Lala":0.003,"Nina":0.005}
u=dict6.pop("Hank",0)#刪除key:value並返回被刪除的value
print(u)

e=dict5.pop("145")
print(e)