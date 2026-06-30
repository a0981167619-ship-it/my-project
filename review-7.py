"""1.def-greet函數"""
def greet(name):
    name=input("請輸入名字:")
    print("Hallo,<%s>!"%(name))
greet('Alice')

"""2.判斷整數是否為偶數"""
def is_even(n):
    n=int(input("請輸入一個數字:"))
    if n%2==0:
        print("True")
    else:
        print("False")
is_even(2)

"""3.def-串列"""
def filter_even(lst):
    new_list1=[]
    for n in lst:
        if n%2==0:
            new_list1.append(n)
    return new_list1
print(filter_even([1,2,3,4,5]))
print(filter_even([10,15,20,25]))

def filter_positive_odd(lst):
    odd=[]
    for n in lst:
        if n>0 and n%2!=0:
            odd.append(n)
    return odd
print(filter_positive_odd([1,-2,3,4,-5,7]))
print(filter_positive_odd([-1,0,2,5,9]))

"""5.def-求立方數的和"""
def sum_of_cubes(n):
    total=0
    for i in range(1,n+1):
        total+=i*i*i
    return total
print(sum_of_cubes(10))

"""求偶數平方的和"""
def sum_square_even(n):
    sum=0
    if n%2==0:
        for i in range(1,n+1):
             if i%2==0:
                 sum+=i*i
        return sum
    else:
        print("不成立")
print(sum_square_even(10))
    
    

        
