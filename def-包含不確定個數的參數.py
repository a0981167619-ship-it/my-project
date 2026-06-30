def pen(mainpen,*exceptpen):
    print('必須用的筆有:',mainpen,'不一定會用到的筆有:')#不確定個數
    for orther in exceptpen:
        print(orther)

pen('原子筆','2B鉛筆','鋼筆')
pen('鋼珠筆','橡皮擦','蠟筆','彩色筆')

def snack(snack2,*orthersnack):
    print("點心有:",snack2,"附餐有:")
    for except1 in orthersnack:
        print(orthersnack)

snack('鬆餅','雞蛋糕','章魚燒','蘋果')#以元組回傳
snack('地瓜球','薯條')
snack('冰淇淋','拔絲地瓜','烤牛奶')

"""偶數總和計算"""
def total(*number):
    Ans=0
    for i in number:
        if i%2==0:
             Ans=Ans+i
             print(Ans)

total(1,2,3,4,5)#呼叫函數

""">10的數字總和"""
def Max(*numbers):
    total=0
    for a in numbers:
        if a>10:
            total=total+a
            print(total)
Max(50,100,0,1,2,3,4,5)#呼叫函數Max()
    
        
       



