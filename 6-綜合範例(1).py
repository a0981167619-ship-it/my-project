"""1.應用串列的sort()函數進行資料的排序(省略reverse()函數)"""
p=[98,46,37,66,69]
print("排列前順序:",p)
p.sort()#將資料進行遞增排列
print("遞增排序:",p)

word=['one','time','happy','child']
print("排列前順序:",word)
word.sort()#將資料進行遞減排序
print("遞減排序:",word)

"""2.串列reverse()函數"""
english=['apple','orange','watermelon']
print('反轉前內容:',english)
english.reverse()#將資料進行反轉
print('反轉後內容:',english)

number=[65,76,54,32,18]
print('反轉前內容:',number)
number.reverse()#將資料進行升冪排列
print("反轉後內容:",number)

"""3.使用sorted()函數,對元組內資料進行排序"""
money=(8000,7200,8300,4700,5500)#建立元組
print(money)
print("由小到大:",sorted(money))#進行升冪排列
print(money)
print("由大到小:",sorted(money,reverse=True))#將資料進行降冪排列
print("資料維持原順序:",money)