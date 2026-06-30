"""刪除到剩三個元素"""
a=[10,20,30,40,50,60]
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)#剩下三個元素

"""反轉名單"""
names=["Amy","Bob","Cindy","David"]
names.reverse()
print(names)

"""不及格名單"""
scores=[55,78,92,60,43]
fail=[]
scores1=int(input())
scores2=int(input())
scores.sort()
print(scores)
if scores1<60:
    fail.append(scores1)
    print("不及格分數:",fail)
    if scores2<60:
        fail.append(scores2)
        print("不及格分數:",fail)
    


