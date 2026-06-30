def change(number):
    number[0],number[1]=number[1],number[0]#交換
print("請輸入兩數值")
number=[]
number.append(int(input()))
number.append(int(input()))
print("number[0]=",number[0])
print("number[1]=",number[1])
change(number)
print("函數交換")
print("number[0]=",number[0])
print("number[1]=",number[1])

"""傳址呼叫((串列))"""
def add_one(nums):
    for i in range (len(nums)):
        nums[i]=nums[i]+1#把串列裡的數字都加1
    print(nums)
numbers=[1,3,5]
add_one(numbers)#呼叫函數

def square_list(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]#把串列裡的數字變成平方
    print(nums)
values=[2,3,4]
square_list(values)


    
