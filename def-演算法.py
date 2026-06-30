def number(x,y):
    for i in range(1,y+1):
        x**=y
        return x
print(number(4,5))#呼叫函數

"""計算平方數"""
def square(x):
    y=x*x
    return y
print(square(5))
print(square(3))

"""計算立方數"""
def cube(x):
    y=x**3
    return y
print(cube(3))
print(cube(5))

"""立方數回傳兩倍"""
def double(x):
    y=(x**3)*2
    return y
print(double(7))



  