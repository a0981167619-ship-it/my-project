"""簡易銀行系統"""
def deposit(blance,money):
    blance=int(input("請輸入目前餘額:"))
    money=int(input('請輸入存入金額:'))
    return blance+money
def withdraw(blance,money):
    blance=int(input("請輸入目前餘額:"))
    money=int(input('請輸入提款金額:'))
    if money>blance:
        print('餘額不足')
def check_blance(blance,money):
    return blance-money


    

    
