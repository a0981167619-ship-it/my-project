"""索引"""
tuple1=("apple","banana","cherry","date")
print(tuple1[0])#索引第一個元素
print(tuple1[3])#索引最後一個元素
print(tuple1[1:3])#索引第二第三個元素

"""二維串列轉二維元組"""
a=[[1,2],[3,4],[5,6]]
print(tuple(map(tuple,a)))#二維串列轉二維元組

"""元組長度與檢查"""
tuple2=("a","b","c","d","e")
print(len(tuple2))#tuple2長度
b="c" in tuple2 #判斷字串c是否在元組中
print(b)
c="z" not in tuple2
print(c)

"""找最大值與最小值"""
temperature=(23,19,25,21,22)
x=print(max(temperature))#找此元組中的最大值
y=print(min(temperature))#找此元組中的最小值
z=temperature[2]-temperature[1]#取最大值最小值算出溫差
print("溫差為:",z)

""""過濾資料與運算"""
tuple3=(12,25,7,30,18,5)
tuple4=()
for k in tuple3:
    if k>15:
        tuple4+=(k,)
        print(tuple4)#把大於15的數添加到新元組tuple4中
        print(sum(tuple4))#計算元組內數字總和

score=(("國文",82),("數學",91),("自然",76),("社會",48),("英文",61))#建立二維元組

score1=[]#建立空串列
for i in  score:
    if i[1]>=70:#保留>=70分的項目,主要判斷在第一元素
        score1.append(i)#符合就添加入串列中
score1=tuple(score1)#串列轉成元組
print(score1)
