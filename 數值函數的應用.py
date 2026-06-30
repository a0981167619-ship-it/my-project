"""統計成績"""
score=[94,89,75,12,30,15,48,56,99]
print("小考次數為:",len(score))
print("所有成績由大到小排序:",sorted(score,reverse=True))
print("所有成績由大到小排序:",sorted(score))#預設reverse=False
print("所有分數總和為:",sum(score))
print("總平均為:",round(sum(score)/len(score),2))#取小數點後兩位
print("考最差的分數為:",min(score))
print("考最好的分數為:",max(score))

"""購物找零"""
price=137.6
paid=200
opaque=abs(paid-price)
print(opaque)
frequence=round(opaque)
print("找零金額為:",frequence)
