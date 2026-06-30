"""找最後一個小於或等於目標的數字索引"""
numbers=[1,3,5,7,9,12,14,18,20]#中間值為9
target=13
def july(list,target):
    left=0
    right=len(numbers)-1
    answer=-1
    while left<=right:
        medium=(left+right)//2
        if list[medium]>target:
            right=medium-5
            answer=right
            return answer
        else:
            left=medium+1
    return -1
north_Hesisphere=july(numbers,target)
print("最後一個小於目標值的為:",north_Hesisphere)

"""找最接近目標數字"""
ticket_prices=[50,80,120,150,200,250]
aim=135
def solution(list,aim):
    left=0
    right=len(ticket_prices)-1
    while left<=right:
        m=(left+right)//2
        if ticket_prices[m]<aim:
            left=m+1
            if abs(ticket_prices[m]-aim)<=30:
                return ticket_prices[m]
        else:
            right=m-1
            if abs(ticket_prices-aim)<=30:
               return ticket_prices[m]
kingdom=solution(ticket_prices,aim)
print("最接近的票價為:",kingdom)
