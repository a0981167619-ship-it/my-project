def sum_function(x,y):
    print("函數內互換前:x=%d,y=%d"%(x,y))
    x,y=y,x#進行函數互換
    print("函數內互換後:x=%d,y=%d"%(x,y))
c=15
k=16
print("函數外互換前:c=%d,k=%d"%(c,k))
sum_function(c,k)#呼叫函數
print("函數外互換後:c=%d,k=%d"%(c,k))#因數值為不可變物件

"""計算正方形體積"""
def cube_volume(side):
    volume=(side)**3
    return volume
length=float(input("請輸入正方形邊邊長:"))
x=cube_volume(length)
print("體積為:%f"%(x))
