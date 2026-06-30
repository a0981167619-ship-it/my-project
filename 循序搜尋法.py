import random
a=[]
for i in range(10):
    a.append(random.randint(1,50))
    print("資料:",a)
aim=int(input("請輸入數字:"))
find=False
for i in range(len(a)):
    if a[i]==aim:
        print("在第{0}個位置找到".format(i+1))
        find=True
        break
    else:
        print("沒有找到")
import random #匯入亂數模組
b=[]#建立空串列
for a in range(15):#串列長度為15
    b.append(random.randint(1,150))#使用random模組,隨機產生1-150的數字
    print("information:",b)#印出整個串列
diligant=int(input("請輸入一數字:"))#請使用者輸入一個數字
turn=False
for a in range(len(b)):
    if b[a]==diligant:
        print("第一次出現的位置為:",i+1)
        turn=True
        break#終止迴圈
    else:
        print("沒有找到")
