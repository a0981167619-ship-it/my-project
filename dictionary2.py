movie={"title":None,"director":None,"year":None}#建立字典,並設定其值為None
while True:
    key=input("請輸入欲查詢的key值:")
    if key in movie:#如果key存在於此字典中
        if movie[key]==None:#且其值為None
            movie[key]=input("請輸入新的值:")
            print(movie)
        else:#若key值不在字典中
            print(movie)#印出此字典
    else:
        movie[key]!=None
        print("自動建立key")

    f=input("continue(Y/N):")#詢問使用者是否要繼續
    if f!="Y":
        break#不繼續則跳出
        
        