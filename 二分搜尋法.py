numbers=[4,9,15,22,27,31,36,40,47,53]
def research(data,aim):
    left=0
    right=len(numbers)-1 #使用index定義
    while left<=right:
        mid=(left+right)//2#找中間值(index定義)
        if data[mid]>aim:#目標在中間值的左邊
            right=mid-1
        elif data[mid]<aim:#目標在中間值的右邊
            left=mid+1
        else:#當目標=中間值,回傳
            return mid
    return -1 #找不到則回傳-1
malevolent=research(numbers,40)
print("目標索引值為:",malevolent)

"""找出第一個>or=目標數字的索引"""
numbers=[3,5,8,10,14,17,20,25,30]#14為中間值
goal=16
def robust(data,goal):
    answer=-1
    left=0
    right=len(numbers)-1
    while left<=right:
        middle=(left+right)//2
        if numbers[middle]<goal:#判斷目標與中間值的位置
            left=middle+1
            answer=left
            return answer
        else:
            right=middle-1
    return -1#找不到就回傳-1
        
index=robust(numbers,goal)
print("第一個目標索引值為:",index)
