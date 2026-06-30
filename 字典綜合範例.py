"""1.基本存取+get"""
dict1={'a':5,'b':10,'c':15}#建立字典
a=dict1.get('b')#印出b的值
print(a)
b=dict1.get('d',0)#因沒有d,傳回預設值為0
print(b)

"""2.fromkeys"""
colors=["red","green","blue"]
k=dict.fromkeys(colors,0)#建立字典,當中所對應的值皆為0
print(k)

"""3.update更新、新增"""
inventory={"apple":10,"banana":5}
inventory.update({"banana":8})#更新字典內數值
inventory.update({"orange":12})#新增元素、數值
inventory.update({"grape":20})
print(inventory)

"""4.條件篩選"""
items={"pencil":10,"pen":25,"rule":15,"notebook":40,"pencil box":120}#建立字典
y={}#建立空字典
for item,money in items.items():
    if money<=20:#保留價格<=20的物品
        y[item]=money
        print(y)

salaries={"Alice":35000,"Bob":28000,"Charlie":42000,"David":30000,"lan":26000}
salary={}
for salarys,money in salaries.items():
    if money>=30000:
        salary[salarys]=money
        print(salary)

"""學生成績統計"""
class1={"Alice":82,"Bob":75,"Charlie":90}
class2={"Bob":88,"David":60,"Alice":95}  #建立字典
scores={}#建立空字典
for name,score in class1.items():
    if score>=80:#取成績大於80者,不符合則被篩選掉
         scores[name]=score
    for name,score in class2.items():
        if score>=80:
            if name in scores:
                 scores[name]+=score #若有重複者,成績相加
            else:
                scores[name]=score          
print(scores)
"""倉庫商品存量"""
warehouse1={"apple":120,"banana":80,"orange":60}
warehouse2={"banana":50,"apple":100,"grape":40}

fruits={}

for fruit,number in warehouse1.items():
    if number>=100:
        fruits[fruit]=number
        for fruit, number in warehouse2.items():
            if number>=100:
                if fruit in fruits:
                    fruits[fruit]+=number
                else:
                    fruits[fruit]=number
total=sum(fruits.values())
print("總數量為:{0}".format(total))
    
    

           
   
        