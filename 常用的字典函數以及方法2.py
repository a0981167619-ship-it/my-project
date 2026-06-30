key1=[1,2,3,4]
dict1=dict.fromkeys(key1,"reveal")#快速建立字典，每個值都會對應到"reveal"
print(dict1)
key2=[5,6,7,8]
dict2=dict.fromkeys(key2,100)
print(dict2)#對應值皆為100
key3=("retreat")
dict3=dict.fromkeys(key3,)#無設定值,預設值為None
print(dict3)

"""dict.get方法"""
dict4={"delicate":10}
a=dict4.get("delicate",)#返回預設值10
print(a)
dict5={"construct":0.001}
b=dict5.get("construction")#字典內沒有construction,返回預設值為None
print(b)

"""key in dict"""

dict6={"sun":2,"cloud":4,"wind":5}
x="sun" in dict6 #sun在dict6中,傳回True
print(x)
y="cloud" not in dict6 #cloud在dict6中,傳回False
print(y)

dict7={"departure":28,"withdraw":150}
z="b" in dict7
print(z)
v="withdraw" not in dict7
print(v)

