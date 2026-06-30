"""choice、sample()"""
tuple1=(1,10,19,28,37)
l='1,2,3,4'
import random
print(random.choice(tuple1))#也支援元組產生的序列(隨機)
print(random.sample(tuple1,4))
print(random.choice(l))#也支援字串產生的序列(隨機)
print(random.sample(l,4))

"""random模組的應用"""
'1.抽獎系統'
students=["Alice","Brian","Cindy","David","Emma","Frank","Grace"]
print('幸運兒為:',random.choice(students))

if random.choice(students)==random.sample(students,3):
    print('幸運兒重複')
else:
    print('候補名單有:',random.sample(students,3))

'2.擲骰子對戰'
player=[1,2,3,4,5,6]
computer=[1,2,3,4,5,6] #玩家與電腦各有六面骰子
print('玩家點數為:',random.choice(player))
print('電腦點數為:',random.choice(computer))
if random.choice(player)==random.choice(computer):#如果玩家隨機的點數與電腦相同
    if random.uniform(0,1)<0.5:#用隨機產生的浮點數來決定
     print('玩家贏')
    else:
        print('電腦贏')
elif random.choice(player)>random.choice(computer):
    print('玩家贏')
else:
    print('電腦贏')

'3.撲克牌發牌'
cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(cards)
print('洗牌後的順序為:',cards)
print('玩家的牌為:',random.sample(cards,5))#隨機抽取5張牌

'4.夏日冰淇淋攤排對抽號碼'
customers=["Alice","Brian","Cindy","David","Emma","Frank","Grace","Henry","Ivy","Jack"]
random.shuffle(customers)
print('抽號順序為:',customers)
print('可得到特別口味的人有:',random.sample(customers,5))#抽出前五個可得到特別口味的人


    

