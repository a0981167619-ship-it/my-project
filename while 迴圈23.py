n=int(input("Please enter an integer:"))
for i in range(2,n+1):
    for j in range(2,int(i**0.5+1)):
        if (n**0.5+1)!=int(i):
            prime=True
        if i%j!=0:
            prime=True
while n%2==0:
    continue
while n%3==0:
    continue
while n%7==0:
    continue
while n%5==0:
    continue
while n%11==0:
    continue
print("The prime number is: %d" %n)
