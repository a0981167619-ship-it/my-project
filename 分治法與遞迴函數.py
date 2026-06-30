"""階乘計算"""
def function(i):
    if i==0:
        return 1#階乘0定義為1
    else:
        answer=i*function(i-1)
        return answer
         
i=int(input("請輸入要階乘的數:"))
print('%d!=%d'%(i,function(i)))

"""雙倍乘積(類似階乘遞迴)"""
def double_product(n):
    if n==1:
        return 2
    else:
        answer=n*double_product(n-1)
        return answer
n=int(input("請輸入一個數:"))
print(double_product(n))

"""累加數字"""
def sum_to_n(n):
    if n==1:
        return 1
    else:
        return n+sum_to_n(n-1)
n=int(input("請輸入一整數:"))
print("累加結果為:%d"%(sum_to_n(n)))

"""數字反轉累加遞迴函式"""
def reverse_sum(n):
    if n<=0:
        return -1
    else:
        sum=n+reverse_sum(n-1)
        return sum
n=int(input("請輸入正整數:"))
print("累加結果為:%d"%(reverse_sum(n)))
