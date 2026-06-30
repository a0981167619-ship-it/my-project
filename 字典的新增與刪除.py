dict1={"number":2,"number1":5,"number2":8}
dict1["number3"]=11#新增元素
print(dict1)

del dict1["number"]#刪除字典中的特定元素
print(dict1)
del dict1#刪除整個字典

dict2={"score":45,"score1":60,"score2":80,"score3":17,"score4":89}
dict2['score5']=100
print(dict2)
del dict2['score']
del dict2['score3']
print(dict2)
del dict2
