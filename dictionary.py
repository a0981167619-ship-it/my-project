car={"brand":None,"model":None,"year":None}#建立字典
while True:
    key=input("請輸入欲搜尋的key:")
    if key in car:#如果key存在於字典中
        if car[key]==None:#且其值為None
            car[key]=input("請輸入新值:")#輸入新值
            print(car)#並印出字典
        else:
            print(car[key])
    else:
        car[key]==None#如果key不存在
        print("自動建立新key")#建立新的key
        print(car)
    d=input("continue(Y/N):")#詢問是否要繼續
    if d!="Y":
        break


    

    
    