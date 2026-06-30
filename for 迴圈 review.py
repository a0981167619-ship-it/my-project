for i in range(1,11):
    print(i)#印出數字1-10

total=0
for k in range(1,11):
    total+=k
print("1-10的總和為:%d"%(total))#找1-10的總和

a=int(input("請輸入一整數:"))
for i in range(1,a+1):
    if i%2!=0:
        continue
    print(i)#找出所有偶數

y=input("請輸入一字串:")
for i in y:
    print(i)#印出字串

for j in range(1,21):
    if j%2==0:
        continue
    print(j)

