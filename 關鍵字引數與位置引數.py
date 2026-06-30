def location(a,b,c):
    sol=a**b+b**c
    return sol

print(location(a=5,b=2,c=10))#呼叫函數,關鍵字引數
print(location(4,c=10,b=0))#位置引數必須在關鍵字引數前
print(location(a=78,b=1,c=0))
print(location(b=25,c=78,a=20))

def solution(x,y,z):
    l=x+y+z
    return l
print(solution(1,2,3))#位置引數
print(solution(x=2,y=6,z=18))#關鍵字引數
print(solution(7890,23,z=65))#關鍵字引數與位置引數混用
