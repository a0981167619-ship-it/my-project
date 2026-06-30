import random #產生隨機數列
organizer=[]
value=10
for _ in range(12):
    organizer.append(value)
    value=random.randint(1,5)
print("數列為:",organizer)
def in_search(organizer,goal):
    left=0
    right=len(organizer)-1
    while left<=right:
        medium=(left+right)//2
        if goal<organizer[medium]:
            right=medium-1
            print("找左半邊")
        elif goal>organizer[medium]:
            left=medium+1
            print('找右半邊')
        else:
            return medium
    return -1

while True:
    goal=int(input("請輸入一個數字:"))
    research=in_search(organizer,goal)
    
    if goal!=-1:
        print("位置為:%d"%(research))
    else:
        print("沒有找到")



    