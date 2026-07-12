"""判斷是否為5或7的倍數 但不能為35的倍數"""

num=int(input("請輸入一數值:"))
if (num%5)==0 or (num%7)==0:
        if(num%35)!=0:
            print("{}為5或7的倍數".format(num))
else:
    print("皆不成立")
        
