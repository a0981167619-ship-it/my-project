W={"math","science","society"}
W.add("English")#新增元素"English"
print(W)

W.remove("society")#移除元素"society"
print(W)

"""add()/remove()"""
n={1,3,5,7,9}
n.add(11)
print(n)

n.remove(5)
print(n)

"""更新或合併元素-update()"""
W.update(n)#把集合合併,重複元素會被忽略
print(W)
v=7 in W
print(v)

r={"robotic","technology"}
g={"global","goal","robotic"}
r.update(g)
print(r)