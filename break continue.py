total=0
for k in range(1,101,3):
    if k==80:
        break    #終止目前指令
    total+=k
print("1~77的數字和為%d"%(total))

#巢狀迴圈
for i in range(3,8,3):
    for k in range(3,8,i+2):
        if k==8:
            break
        print(k,end="")
    print()

for a in range(1,20):
    if a==18:
        continue   #跳過此敘述
    print(a)

for b in range(2,10,5):
    if b==7:
        continue
    print(b)

#求π值
k=int(input("請輸入一整數:"))
total=0
for i in range(int(k)+1):
    if i%2==0:
        total+=float(1/(2*i+1))
    else:
        total+=float(-1/(2*i+1))  #i為奇數時
print("π 值為=%f"%(total*4))
i+=2

