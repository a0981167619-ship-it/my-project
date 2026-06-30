a=input("請輸入數字:")
print("Luck number")

X=input("請輸入身高:")
Y=input("請輸入體重:")
Z=input("請輸入性別:")
B=input("請輸入年齡:")

print("女生基礎代謝率",10*int(Y)+(6.25*int(X))-(5*int(B))-161) #女生BMR

print("男生基礎代謝率",10*int(Y)+(6.25*int(X))-(5*int(B))+5)   #男生BMR

O=input("請輸入餘額:")
print(float(O)*1.96)

"""
第一題
"""
year=input("請輸入年:")
month=input("請輸入月:")
day=input("請輸入日:")
print("日期%s-%s-%s"%(year,month,day)) #%格式化輸出
print("{}年{}月{}日".format(year,month,day)) #format格式化輸出


'''
第二題
'''
weight=input("請輸入體重:")
print("月球上的體重為:%1.3f"%((float(weight)*0.17)))

"""
第三題
"""
number=input("請輸入十進位數:")
print("%s的八進位是:%o"%(number,int(number)))
print("%s的十六進位是:%x"%(number,int(number)))
