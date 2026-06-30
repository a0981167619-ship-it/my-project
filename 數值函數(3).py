"""sorted()函數"""
list1=[2,7,899,106,54]
genuine=sorted(list1)#預設值為False,將串列元素進行升冪排列
print(genuine)

generous=sorted(list1,reverse=True)#將串列元素進行降冪排列
print(generous)

list2=[5.98,8.97,4.06]

uncertain=sorted(list2)
print(uncertain)
worthy=sorted(list2,reverse=True)
print(worthy)

"""max()函數"""
list3=[10,75,10.75,999]
print(max(list3))#返回串列元素中的最大值
print(max(list2))

"""min()函數"""
print(min(list3))#返回串列元素中的最小值
print(min(list1))

"""len()函數"""
list4=["disgusting","unworthy","opaque"]
print(len(list4))#傳回串列元素個數
print(len(list3))

"""sum()函數"""
list5=[1,2,3,4,5,6,7,8,9,10]
print(sum(list5))#將串列元素進行加總
print(sum(list2))