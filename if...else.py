score=int(input("請輸入分數:"))
if score>=60:
    print("%d  good"%score)
else:
    print("%d  再加油"%score)

"""
判斷是否為2或3的倍數 不能為6的倍數
"""
number=int(input("請輸入一個整數:"))
if number%2==0 or number%3==0:
    if number%6!=0:
        print("條件符合")
    else:
        print("條件不符合")
else:
    print("error")

"""
讓使用者輸入西元年(4位數的整數year),判斷是否為閏年,滿足兩條件之一即為閏年:
1.逢4年閏(除4可整除)但逢100年不閏(除100不可整除)
2.逢400年閏(除400可整除)
"""
year=int(input("請輸入一個四位數:"))
if year%4==0 and year%100!=0:
    if year%400==0:
        print("%s是閏年"%year)
    else:
        print("%s不是閏年"%year)
else:
    print("%s不是閏年"%year)

"""
if-成績判斷
"""
score=int(input("請輸入分數:"))
if score>100:
    print("分數超過100 Error")
else:
     if score<0:
                print("負數分數不符合條件")
     else:
        if score>=60:
                     print("分數{}分 考得不錯".format(score))
        else:
             if score<60:
                      print("分數{}分 要再加油".format(score))

"""
判斷是否為7與8的公倍數
"""
n=int(input("請輸入一個數:"))
if n%7==0:
    if n%8==0:
        print("{}是7與8的公倍數".format(n))
else:
    print("{}不是7的倍數".format(n))
