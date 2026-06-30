x,y=0,10
while x<y:
    x=x+1
    if x==6:
        continue
    print(x)

i=0
while i<=10:
    i=i+1
    if i%2==0:
        continue
    print(i)


i=1
while i>0:
    n=int(input("請輸入一整數:"))
    if n>0:
        i+=n
        print("總和為%d"%(i))
    if n<0:
        continue
    i=i-1


    
    
        
    
