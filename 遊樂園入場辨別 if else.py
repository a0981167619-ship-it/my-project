height=float(input("Please enter your height:"))
r=input("Please enter whether you are accompanied by a parent:")
if (height<100):
    if r=="True":
        print("Can be shortlisted")
    else:
        print("Cannot be shortlisted")
elif(100<=height<120):
    print("Parents must be present to enter")
else:
    print("Free entry")

