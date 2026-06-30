Ans=input("請輸入一個數字:") #字串
print(bool(Ans)) #不管輸入什麼都為True

X=float(input("請輸入腰圍:"))
Y=float(input("請輸入臀圍:"))

print(X/Y)

if (X/Y<=0.8):
    print("低風險")
elif(X/Y>0.86):
    print("高風險")  #女生腰臀比
else:
    print("中風險")

YEAR=input("請輸入出生年:")
MONTH=input("請輸入出生月:")
DAY=input("請輸入出生日:")
print("%s/%s/%s"%(YEAR,MONTH,DAY))
print("{}/年{}/月/{}日".format(YEAR,MONTH,DAY))

number=input("請輸入1個數字:")
print("%s的指數e形式為:%e"%(number,float(number)))

num1=input("請輸入1個數字:")
h=int(num1)
print("%s的二進位為:%s"%(number,bin(h)))
