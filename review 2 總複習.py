
x=1
print(x)
X="lemon"
print(X)

x=10;y=10
print(x,y)
x=y=z=10
print(x,y,z)
a,b,c=10,10,10
print(a,b,c)
num,city,country=100,"Taipei","Taiwan" #可混合不同資料型態一起宣告
print(num,city,country)

sum=123465789969965656556
del sum                                          ###2-1複習
print(sum)

sum=8
sum=sum+1
print(sum)

number=9
number1=10
print(number1+number)

tiger,lion,monkey="老虎","獅子","猴子"

__fgohk=8989
print(__fgohk)
"""
底線變數符合變數定義規則
"""
海龜="turtle"
print(海龜)

'''
中文變數也符合變數定義規則
'''

###2-2複習
"""
Z進位的轉換
"""

n=999
print(n)
n1=bin(n) #十進位變二進位
print(n1)
n2=oct(n) #十進位變八進位
print(n2)
n3=hex(n) #十進位變十六進位
print(n3)
print(int(n1,2))
print(int(n2,8))
print(int(n3,16)) #int(s,base)做轉換

'''
浮點數的資料型態
'''
violence=float.fromhex('0x5.Ep2') 
print(violence)
regular=float.fromhex('0xA.Ep10')   ###將十六進位的浮點數轉為十進位
print(regular)
clumsy=float.hex(23.66)
print(clumsy)
clever=float.hex(777.0)             ###以字串回傳十六進位的浮點數
print(clever)
intelligence=9.0
print(float.is_integer(intelligence)) ###is_integer辨別是否為整數 小數點位數為0時會回傳True
intelligent=45.65
print(float.is_integer(intelligent))  ###不為0時會回傳False
triumph=7.8787888878787
print(round(triumph,5)) #前面不需float做引導,會回傳最靠近triumph的數值(取5位)
north=(0.2*0.3)
print(round(north,3))

"""
布林值
"""
c=bool(0)
print(c)
jellyfish=bool(1)
print(jellyfish)
diet=bool(   )
print(diet)
weird=bool("  ")
print(weird)
yellow=bool("APPLE,APPRECIATE")
print(yellow)
stimulate=bool("0")
print(stimulate)
__decay=bool("") ###字串裡沒放東西或空白格 一樣為False
print(__decay)

'''
資料型態
'''
operate="gentle"
print(operate)
__h="1*2"
print(__h)
print("It\'s dog.\
isn't it?")
satisfy="My name is Joe.\
What is your name?"
print(satisfy)
satisfaction="I'm twenty five years old"
print(satisfaction)
satisfying='I\'m twenty five years old'
print(satisfying)
destroy="where\
 is\
 a\
 movie\
 theater?"
print(destroy)

print("""蝸牛
蛞蝓
青蛙
福壽螺""")
print('''cheese
tomato
seafood
steak''')

"""
資料型態的轉換
"""
entertainment=2.5
print(type(entertainment))   ###用type辨別資料型態的類型
acquire=56
print(type(acquire))
cometogether="I LOVE YOU"
print(type(cometogether))
cometogether=True
print(type(cometogether))

sum=100+0.5
print(sum)

print("I'm"+ "tired")

composition=3.6
q=2+int(composition) #浮點數轉為整數
print(q)

ingredient="7.8"
o=17+float(ingredient) #字串轉為浮點數
print(o)

etiquette="23"
you=23+int(etiquette)
print("數值為:"+str(you))

"print函數()"
print(456,789,101112,sep="☠")
print(456,789,101112)
print("SO good")
print("so","good",sep="☻")
print("so","good",sep="☻",end="  ")#使用end使輸出在同一行
print("not","really",sep="☻") #用sep取代空白格

"[%] 格式化輸出"
ty=400
print("數字的數值為:%d"%(ty))

print("%s800公尺接力時間為:%2.3f"%("紅隊",25))
print("%s800公尺接力時間為:%2.3f"%("藍隊",30))

num=365
print("數字%s的浮點數為:%1.1f"%(num,num))
print("數字%s的二進位為:%s"%(num,bin(num)))
print("數字%s的八進位為:%o"%(num,num))
print("數字%s的十六進位為:%x"%(num,num))

rose=9.18
print("%s的浮點數指數e形式為:%e"%(rose,rose))

flower=3.666
print("%s的浮點數指數e形式為:%e"%(flower,flower))

'''
format格式化輸出
'''
print("{0}英文考了{1}分".format("Andy",80))

print("{name}擁有一個{item}".format(name="Tom",item="car toy"))

print("{0:.5}".format(7888.656)) #取5位數
print("{0:.10}".format(9777.2345679892)) #取10位數

money=65000
bag=35000
watch=30000
print("{}+{}={}".format(bag,watch,money))

str="{0}/{1}={2}"
x="98"
y=98
print(str.format(x,y,int(x)/y))

print("{0:8}居住在:{1:♡^10}".format("Paula","USA")) #沒填滿的用heart填入並置中
print("{0:8}居住在:{1:𓅇>15}".format("Paul","Australia")) #沒填滿的用bird填入並靠右
print("{0:8}居住在:{1:❀<10}".format("PiPi","UK")) #沒填滿的用flower填入並靠左

print("班級  姓名 座號  分數")
print("%d   %s   %d   %3.1f"%(101,"Bob",15,85.6))
print("%d   %s  %d   %3.1f"%(103,"Hank",56,77.8)) #用[%]格式化輸出分數
print("%d   %s  %d   %3.1f"%(105,"KiKi",23,99.6))
print("{C}   {name}  {seat}   {score}".format(C=106,name="David",seat=6,score=56.5)) #用format格式化輸出分數

"""
輸入指令--input
"""
x=input("請輸入百位數:")
y=input("請輸入個位數:") #輸入的數值做運算
print(int(x)*int(y))

salary=input("請輸入您的薪水:")
money=input("請輸入您的花費:")
tax=input("須繳納的稅金:")
print("您的薪水為%d 您花費的為%d 您須繳納的稅金為%d"%(int(salary),int(money),int(tax))) #[%]格式化輸出
print("薪水為:{} 花費為:{} 需繳納的稅金為:{}".format(salary,money,tax)) #format格式化輸出

jump=input("請輸入你在地球上的跳躍高度:")
moon=int(jump)*6
print("你在月球上的跳躍高度為:",moon)

number=input("請輸入一個十進位數字:")
print("%s的八進位為:%o"%(number,int(number)))
print("%s的十六進位為:%x"%(number,int(number)))#請使用者輸入一個十進位數字 做二進位,八進位,十六進位的轉換
XY=int(number)
print("%s的二進位為:%s"%(number,bin(XY)))






