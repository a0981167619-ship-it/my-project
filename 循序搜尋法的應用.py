"""學校點名系統"""
students=[3,7,12,5,7,9,2]
target=int(input("請輸入一個座號:"))
count=0
for i in range (len(students)):
    if students[i]==target:
        print("第%d位同學是你"%(i+1))
        count+=i
        print("總共有幾位同學找到這個座號:",count)
   
    else:
        print("沒有這個座號")

"""找出最小值的位置"""
numbers=[12,7,5,9,5,8]
minimal=min(numbers)
print("最小值為:",minimal)
for i in range(len(numbers)):
    if numbers[i]==min(numbers):
        print("最小值第一次出現的位置為:",i+1)
    if numbers[i]==min(numbers):
        c=numbers.count(5)
        print("最小值出現的總次數為:",c) 
    
