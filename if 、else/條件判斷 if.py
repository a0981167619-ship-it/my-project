"""
Q1:某一百貨公司準備年終回饋顧客,請使用if指令來設計只要所輸入的消費額滿2000則即贈送來店禮
"""
money=int(input("請輸入消費額:"))
if (money>2000): print("請到櫃台領取來店禮")

"""
Q2:請讓使用者輸入一個數值,並可由所輸入的數值去選擇計算立方值或平方值
"""
#if 數值 =2 ---計算平方值
#if 數值 =3---計算立方值

a=input("請輸入2或3:")
if a=="2":
    answer=int(a) #計算平方值
    ANS=(answer*answer)
    print("平方值為:%d"%ANS)
if a=="3":
    answer=int(a) #計算立方值
    A=(answer*answer*answer)
    print("立方值為:%d"%A)
