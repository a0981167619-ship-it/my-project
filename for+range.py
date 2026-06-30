for i in range(10,0,-1):
    print(i)#印出10-1

x=int(input("請輸入一整數:"))
for a in range(1,x+1):
    if a%4==0:
        print(a)

a=input("請輸入一字串:")
for index,i in enumerate(a):
    print("{0}-{1}".format(index,i))#索引值

y=int(input("請輸入一整數:"))
for i in range(1,y+1):
    if i%3==0:
        print("Fizz")
    if i%5==0:
        print("Buzz")
    if i%3==0 and i%5==0:
        print("FizzBuzz")

for x in range(1,10):
    for y in range(1,x+1):
        if y==5:
            break
        print(y,end="")

