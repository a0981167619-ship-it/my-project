succeed=[None]*1000
def f(n):
    result=succeed[n]

    if result==None:
        if n==0:
            result=0
        elif n==1:
            result=1
        else:
            result=f(n-1)+f(n-2)
        succeed[n]=result
    return result
        
n=int(input("計算幾個費式數列:"))
for i in range(n+1):
    print(f(i))

"""最短跳躍數列和"""
a=[None]*1000
def seq_dp(n):
    sum=a[n]

    if sum==None:
        if n==0:
            sum=0
        elif n==1:
            sum=1
        else:
            sum=seq_dp(n-1)+seq_dp(n-2)
        a[n]=sum
    return sum
        
n=int(input("請輸入一整數:"))
for i in range(n+1):
    print("數列和為:",seq_dp(i))


        
            
            
    
   
    


        

