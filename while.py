o=2
y=int(input("請輸入一偶數:"))
while o<y:
    if y%2==0:
        print("<%d的所有偶數為%d:"%(y,o))
        o+=2
