"""Q1:某馬路長960公尺,每隔15公尺要種一棵樹,包含起點與終點 若每棵樹要花費1200元
請寫一程式計算總共需要花費多少元?
"""
a=(960/15+1)*1200
print("共要花費%d元"%a)

"""Q2:設計一程式,輸入一個至少四位數的數,並利用[整數除法//]與[餘數運算%]來輸出其千位數的數字
"""
x=input("請輸入一個>=四位數的數:")
y=int(x)
z=(int(y/1000)%10) #取一位數
print(z)

"""
Q3:設計一程式,讓使用者輸入需兌換的金額,並輸出所需的500元鈔票 100元鈔票 50元硬幣數量
"""
coin=input("請輸入金額:")
five_hun=(int(coin)//500)
one_hun=(int(coin)-five_hun*500)//100
fifty_coin=(int(coin)-five_hun*500-one_hun*100)//50
print("500元有%d張 100元有%d張 50元硬幣有%d個"%(five_hun,one_hun,fifty_coin))
print("500元有{}個 100元有{}個 50元硬幣有{}個".format(five_hun,one_hun,fifty_coin))
