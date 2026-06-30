"""二分搜尋找目標數字是否存在"""
shelf_numbers=[2,5,8,11,14,17,20]
target=14
def retreat(data,target):
    left=0
    right=len(shelf_numbers)-1
    while left<=right:
        mid=(left+right)//2
        if shelf_numbers[mid]<target:
            left=mid+1
            print("找到")
    else:
        print("沒找到")
diligant=retreat(shelf_numbers,target)
print()
