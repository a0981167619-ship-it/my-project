"""divmod()函數"""
answer=divmod(75,16)
print('75/16商為:',answer[0])#取兩數相除的商
print('75/16的餘數為:',answer[1])#取兩數相除的餘數

Ans=divmod(270,45)
print('270/45商為:',Ans[0])
print('270/45餘數為:',Ans[1])

"""pow()函數"""
realistic=pow(2,10)#輸出2**10
print(realistic)
unrealistic=pow(2,10,5)#2**10/5取%
print(unrealistic)

predictable=pow(3,9)
print(predictable)
pessimism=pow(3,9,3)#3**9取%
print(pessimism)

"""round()函數"""
negative=round(45.6)#當沒有y參數,數值為四捨六入
print(negative)
positive=round(1.232323,2)#有y參數,用來設定有幾位小數
print(positive)
arrogant=round(45.5)#看前一位決定,前一位為奇數,進位
print(arrogant)

just=round(3.7781,1)#四捨五入
print(just)
unjust=round(78.5)#前一位為偶數,無y參數,捨去
print(unjust)
optimism=round(45.4)#當沒有y參數,數值為四捨六入
print(optimism)

"""chr()函數"""
logical=7000
print(chr(logical))#取logical字元
unlogical=3025
print(chr(unlogical))

"""str()函數"""
typical=0.4771
print(str(typical))#將數值轉成字串
decline=2187
print(str(decline))
