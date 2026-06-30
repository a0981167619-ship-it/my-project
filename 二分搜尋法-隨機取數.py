import random
list=[]
i=3
for _ in range(18):
    list.append(i)
    i=random.randint(2,6)
print("數列為:",list)
#二分搜尋
def find(list,k):
    left=0
    right=len(list)-1
    while left<=right:
        mid=(left+right)//2
        if k<list[mid]:
            right=mid-1
            print("找左半邊")
        elif k>list[mid]:
                left=mid+1
                print("找右半邊")
        else:
            return mid
    return -1

while True:
    k=int(input("請輸入一個整數:"))
    emphasize=find(list,k)
    if k!=-1:
        print("位置為%d"%(emphasize))
    else:
        print("沒有找到")
            