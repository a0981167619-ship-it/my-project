animal=["cat","frog","snake","dog","lion","fish","bird"]#建立一維串列

addanimal=str(input("請輸入新增動物:"))

if animal.count(addanimal)==0:
    animal.insert(len(animal)-3,addanimal)

print("搜尋新增動物索引位置:",animal.index(addanimal))

animal1=animal.copy()
animal.clear()

print("複製原串列:",animal1)
print("原串列:",animal)

x=int(input("請輸入人數:"))
y=[]
print("請輸入{0}個數值:".format(x))

for i in range(1,x+1):
    score=int(input())#取得輸入數值
    y.append(score)#新增到串列

print("總共輸入的分數:",end='\v')
for i in y:
    print("{:2d}".format(i))
