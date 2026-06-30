n=int(input("Please enter your math score:"))
score=int(input("Please enter your Chinese language scores:"))
c=int(input("Please enter your English score:"))
a=(n+score+c)/3
if (a>=90):
    if(n>=85):
        if(score>=85):
            if(c>=85):
                print("Distinguished Scholarship")
            else:
                print("General scholarship")
elif (80<=a<89):
    print("perform well")
else:
    print("Not eligible for scholarship")
