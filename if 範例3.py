"""
請設計一程式,已經有一個樂透號碼,讓使用者輸入任意一個整數,如果猜對了則結束程式,不對則列出猜錯字樣
"""
number=77
num=int(input("請輸入您所猜的數值:"))
if num!=number:
    print("猜錯了")
    print("正確答案為:%d"%number)
