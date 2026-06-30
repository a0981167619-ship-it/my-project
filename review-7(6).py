"""16.疊代法-連乘偶數總和"""
def f(n):
    total=1
    for i in range(2,n+1,2):
        total*=i
    return total
print(f(6))

"""累加平方和"""
def function(n):
    total=0
    for i in range(1,n+1):
        total+=i*i
    return total
print(function(5))

"""連乘奇數"""
def cooperate(n):
    total=1
    for i in range(1,n+1,2):
        total*=i
    return total
print(cooperate(5))

"""連加奇數平方總和"""
def t(n):
    total=0
    for i in range(1,n+1,2):
        total+=i*i
    return total
print(t(6))

"""階乘奇數、偶數分組總和"""
def wisdom(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum
n=int(input("請輸入一個正整數:"))
total=0
for i in range(1,n+1,2):
    total+=wisdom(i)
print('奇數總和為:',total)

def intelligent(n):
    sigma=1
    for i in range(1,n+1):
        sigma*=i
    return sigma
n=int(input("請輸入一個正整數:"))
total=0
for a in range(2,n+1,2):
    total+=intelligent(a)
print("偶數階乘總和為:",total)

"""累加倍數總和"""
def four(n):
    total=0
    for i in range(1,n+1):
        if i%4==0:
            total+=i
    return total
print(four(15))
        


    

  
        
 
        

 
  


  


   

 