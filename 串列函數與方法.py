"""常用的串列函數以及方法"""
'''函數'''
list1=["ABCD",0.3456,True,"commence",456789]
print(len(list1))#返回串列元素個數
list2=[123,456,0.000001,78900000,3.1415626535,10000000]
print(len(list2))
print(max(list2))#返回串列元素中最大值
print(min(list2))#返回串列元素中最小值

'''常用方法'''
list3=["fragile","weak","strong","brave","brave"]
list3.append("brave")#串列末尾處新增一筆元素
print(list3)
print("brave出現的次數:",list3.count("brave"))#返回串列重複出現的次數
list3.extend("decrease")#串列末尾處新增多筆元素
print(list3)
list3.insert(2,"encourage")#在串列指定位置插入元素
print(list3)


list4=["foolish","fool","stupid","fool","stupid"]
list4.append("foolish")
print(list4)
print("foolish出現的次數:",list4.count("foolish"))
list4.extend("compress")
print(list4)
list4.insert(3,"reaction")
print(list4)
