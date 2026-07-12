K=int(input("Please enter the temperature in Celsius:"))
_C=(K*9/5)+32
print(_C)
if _C<=0:
    print("Below freezing point")
elif _C>=100:
    print("above boiling point")
else:
    print("general temperature")
