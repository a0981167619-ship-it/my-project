'''抽獎活動'''
import random
participants=['Alice','Bob','Charlie','David','Eva','Frank','Grace','Hannah']
random.shuffle(participants)
print('得獎者:',random.sample(participants,5))

'''範例-random'''
a=[1,2,3,4,5,6,7,8,9,10]#從1-10裡隨機抽取5個整數
print(random.sample(a,5))
word=['apple','bird','tiger','quick','happy']
random.shuffle(word)
print(word)

