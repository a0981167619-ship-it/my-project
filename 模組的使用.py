import random
'''random模組'''
c=random.randint(1,200)#隨機從1-200中產生亂數
print(c)

b=random.randint(1,999)
print(b)

'''另一種產生亂數的方式'''
from random import *
c=randint(1,20)
print(c)

from random import *
b=randint(56,789)
print(b)

'''使用別名.函數名稱呼叫'''
import random as ran
print(ran.randint(1,150))#產生1-150的亂數

import turtle as t
tur=t.forward(100)
print(tur)
