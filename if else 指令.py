"""
分數判斷
"""
x=int(input("請輸入分數:"))
if (x>=60):
    print("PASS")
else:
    print("Fail")

"""
3的倍數判斷
"""
a=int(input("請輸入數值:"))
if (a%3)==0:
    print("a是3的倍數")
else:
    print("a不是3的倍數")

print('{0}'.format("a是3的倍數" if (a%3)==0 else print("a不是3的倍數")))
