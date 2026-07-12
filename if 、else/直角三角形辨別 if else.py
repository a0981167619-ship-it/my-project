
a=int(input("Please enter the first side length:"))
b=int(input("Please enter the second side length:"))
c=int(input("Please enter the third side length:"))
if (a+b<=c):
    print("not a triangle")
if(b+c<=c):
    print("not a triangle")
if (a==b==c):
    print("equilateral triangle")
if(a==b or b==c or a==c):
    print("isosceles triangle")
else:
    if a**2+b**2==c**2:
        print("equilateral triangle")
    else:
        print("General triangle")
