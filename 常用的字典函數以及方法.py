"""常用的字典函數"""
dict1={"n":0.236,"g":0.238,"h":0.235}
dict2={"a":0.123,"f":0.128,"t":0.896,"o":0.456456456,"l":1.235}
print(len(dict1))#計算dict1字典元素個數,即key的總數
print(len(dict2))#計算字典dict2元素個數
print(str(dict1))#以字串的方式輸出字典dict1的key:value
print(str(dict2))#以字串的方式輸出字典dict2的key:value

"""常用的字典方法"""
dict1.copy()#複製dict1字典
print(dict1)
dict2.copy()#複製dict2字典
print(dict2)
dict1.clear()#清空dict1字典
print(dict1)
dict2.clear()#清空dict2字典
print(dict2)
