ans=lambda x,y:x+y#使用lambda函數取代def
number1=0
number2=0
number1=int(input("請輸入一整數:"))
number2=int(input("請輸入一整數:"))
print("數值總和為:",ans(number1,number2))

"""lambda函數"""
calc=lambda a,b:a*b
a=int(input("請輸入參數a:"))
b=int(input("請輸入參數b:"))
print("相乘結果為:",calc(a,b))#呼叫函數

