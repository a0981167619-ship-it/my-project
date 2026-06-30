"""階乘平方和"""
def factorial_odd_square_sum(n):
    x=1
    total=0
    for i in range(1,n+1):
            x*=i
            total+=x*x
    return total
        
print(factorial_odd_square_sum(4))
print(factorial_odd_square_sum(3))

"""階乘立方和"""
def factorial_cube_sum(n):
      y=1
      total=0
      for i in range(1,n+1):
            y*=i
            x=y*y*y
            total+=x    
      return total
print(factorial_cube_sum(5))

"""階乘能被3整除的立方和"""
def factorial_div3_square_sum(n):
      z=1
      total=0
      for a in range(1,n+1):
            z*=a#每次更新數字
            b=z*z
            if z%3==0:
                  total+=b
      return total

print(factorial_div3_square_sum(3))
            

    
