"""特殊跳法(只能走2或3步)"""
hesitant={}
def ways(L):
    if L in hesitant:
        return hesitant[L]
    if L==0:
        return 1
    elif L==1:
        return 0
    elif L==2:
        return 1
    else:
        hesitant[L]=ways(L-2)+ways(L-3)
        return hesitant[L]
print(ways(3)) #因1+0=1
print(ways(6))#f(1)+f(1)+f(2)+f(2)=2

"""可以走1步或4步"""
generous={}
def method(L):
    if L in generous:
        return generous[L]
    if L<0:
        return 0
    elif L==0:
        return 1
    else:
        generous[L]=method(L-1)+method(L-4)    
        return generous[L]
print(method(6)) #可用1、4排4種不同的方法 ex.1+1+1+1+1+1=6
#4+1+1=6
#1+1+4=6
#1+4+1=6 共4種
print(method(9))


