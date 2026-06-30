def f(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        answer=f(n-1)+f(n-2)
        return answer
n=int(input("請輸入一整數:"))

for n in range(n+1):
    print("f(%d)=%d"%(n,f(n)))

"""跳號數列累加"""
def seq_sum(n):
    if n==0 or n==1:
        return 1
    else:
        sum=seq_sum(n-1)+3
        return sum
n=int(input("請輸入一整數:"))
print(seq_sum(n))


        
   
    