"""6.lambda函數"""
add_five=lambda x:x+5
print(add_five(3))
print(add_five(10))

square_minus_two=lambda x:(x**2)-2
print(square_minus_two(3))
print(square_minus_two(5))

"""7.lambda-條件判斷"""
elaborate=lambda x:x*3 if x%2!=0 else x//2
print(elaborate(5))
print(elaborate(8))

f=lambda n:print("big") if n>100 else print("small")
print(f(150))
print(f(80))

"""8.階乘計算"""
def f(n):
    total=1
    if n==1:
        return 1
    for i in range(1,n+1,2):
        total*=i
    return total

print(f(5))
print(f(6))##因為6是偶數,所以不乘
print(f(1))

"""階乘平方和"""
def similar(n):
    total=1
    if n<1:
        return 1
    for i in range(1,n+1):
        i=i*i
        total*=i
    return total

print(similar(3))
print(similar(4))
print(similar(1))

    
      
