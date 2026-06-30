"""移除元素-pop()"""
dict1={"material":"Hg","0.4771":0.4771,"0.8451":"log7"}
dict1.pop("0.4771")#刪除指定元素
print(dict1)
dict1.pop("material")
print(dict1)

"""更新或合併元素-update()"""
dict2={"material":"Br","resource":789}
dict1.update(dict2)#有重疊元素將直接取代                                                                                                                                      
print(dict1)
dict3={"%":0.8,"$$$":10000000}
dict3.update(dict1)
print(dict3)

"""items()、keys()、values()"""
print(dict2.items())#取得此字典的key與value
print(dict2.keys())#取得此字典的key
print(dict2.values())#取得此字典的value
dict4={"27**2":729,"32**2":1024,"32/4":8}
print(dict4.items())
print(dict4.keys())
print(dict4.values())