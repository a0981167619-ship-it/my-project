print("{0}一個禮拜掃地{1}次".format("Eason",5))

print("{exam}{cheat}分數為{score}".format(exam="考試",cheat="作弊",score=0))

print("{0:.4}".format(2.238579))

city="高雄"
weather="晴朗"
print("{}天氣為{}".format(city,weather))

str="{0}*{1}={2}"
x=300
y="300"
print(str.format(x,y,x*int(y)))

print("{0:4}跑步秒數{1:_^6}".format("Owan",16))
print("{0:4}跑步秒數{1:>6}".format("Paul",45))
print("{0:4}跑步秒數{1:&<6}".format("John",6))

print("座號","分數","排名")
print("%1s %2d %2d"%("1",120,5))
print("%1s %2d %2d"%("2",89,10))
print("%1s %2d %2d"%("45",220,1))

print("{number}號的分數為{score}排名為{x}".format(number="78",score="38",x="500"))
print("{number}號的分數為{score}排名為{y}".format(number="36",score="66",y="450"))
print("{number}號的分數為{score}排名為{z}".format(number="12",score="12",z="600"))

print("{0}一個禮拜運動{1}分鐘".format("Bella",150)) #{}必須為0,1

print("{person}月薪為{money}".format(person="Kevin",money=10000000000))
print("{0:>.5}".format(30.169))
animal="crab"
place="ocean"
print("{}在{}裡".format(animal,place))
str="{0}*{1}={2}"
a=45
b="20"
print(str.format(a,b,a/int(b))) #輸出格式為a*b=x

print("{0:4}年薪為{1:_^12}".format("Andy",120000))
print("{0:4}年薪為{1:%>12}".format("Kayla",1200000))
print("{0:4}年薪為{1:<12}".format("Eva",12000000000))

print("年","月","日")
print("%1d,%2d,%3d"%(1966,2,3))
print("%1d,%2d,%3d"%(1945,12,16))
print("%1d,%2d,%3d"%(1216,4,5))

year="1958"
month="6"
day="30"
print("{}年{}月{}日".format(year,month,day))
