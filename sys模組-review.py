import sys
'''計算零用錢總和'''
allowance=sys.argv[1:]#從第二個開始

allowance=[int(a) for a in allowance]#把a換成整數

total=sum(allowance)

print('輸入數字:',allowance)
print('總和為:',total)

'''找出最高花費'''
max_money=sys.argv[1:]
max_money=[int(i) for i in max_money]
sum=max(max_money)
print('最高花費為:',sum)

