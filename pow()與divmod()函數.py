"""pow()函數"""
a=pow(5,3)#輸出為5的3次方
print(a)
b=pow(5,4,50)#輸出為5的4次方,跟50取餘數
print(b)

"""divmod()函數"""
end=divmod(98,8)
print("98/8商為:",end[0])
print('98/8餘數為:',end[1])

money=int(input("請輸入剩餘金額:"))
people=int(input("請輸入總人數:"))
result=divmod(money,people)
print("每人可分到{0}元".format(result[0]))
print("剩餘的錢為{0}元".format(result[1]))#取餘數

"""時間轉換-divmod()"""
sec=int(input("請輸入總秒數:"))
ans=divmod(sec,60)
print("總共為%d分鐘"%(ans[0]))
print("剩餘秒數為:%d秒"%(ans[1]))