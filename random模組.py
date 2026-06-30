import random

"""random.random()"""
ill=random.random()#產生0-1的隨機浮點數
print(ill)

"""random.randint()"""
illness=random.randint(1,999)#隨機產生指定範圍內的整數
print(illness)
s=random.randint(1,10)
print(s)

"""random.uniform()"""
a=random.uniform(1,500)#隨機產生指定範圍內的浮點數
print(a)
astronaut=random.uniform(1,40)
print(astronaut)

"""random.randrange()"""
stable=random.randrange(101,200,3)#於指定範圍的序列中取得一個亂數
print(stable)
gain=random.randrange(50,60,2)
print(gain)

"""random.choice()"""
list1=[10,60,450,123,456]
print(random.choice(list1))#從序列中取得一個隨機元素
list2=[0,0,1,1,2,3,5]
print(random.choice(list2))

"""random.sample()"""
list3=[7.08,4.56,9.00,1.00,2.03]
print(random.sample(list3,3))#從序列中取得k指定範圍內長度的元素(隨機)
list4=[5.06,1,3.04,3.14,5,0,0,1]
print(random.sample(list4,5))

"""random.shuffle()"""
list5=[99,100,101,130]
random.shuffle(list5)#序列中隨機排序
print(list5)
list6=[8.0,1.2,4.5,6.9,8.7]
random.shuffle(list6)
print(list6)