print("never")
print("1","2","3")
print("1","2","3",sep="%")
print("1","2","3",sep="%",end="")
print("1+2+3")
print(1998)         #sep,end的使用
print(1998,2550,3516)
print(1998,2550,3516,sep="--")
print(1998,2550,3516,sep="--",end="")
print(1945)

'''[%]格式化輸出
'''

rabbit="胡蘿蔔"
print("rabbit愛吃%s"%rabbit)

print("%s排位積分%2.3f"%("Eason",156))
print("%s排位積分%2.3f"%("Gary",200))

numX=333
print("%s的浮點數為%3.1f"%(numX,numX))
print("%s的八進位為%o"%(numX,numX))
print("%s的十六進位為%x"%(numX,numX))
print("%s的二進位為%s"%(numX,bin(numX)))
print("%s的浮點數(指數e)為%e"%(numX,numX))

NUMy=178
print("%s的二進位為%s"%(NUMy,bin(NUMy)))

ti=156
print("%s的二進位為%s"%(ti,bin(ti))) #為整數二進位 不可以為浮點數

"""format格式化輸出
"""

print("{0}的資產為{1}".format("KuKu",1000000000000000000000000000))

print("{indoor}溫度為{temperature}".format(indoor="百貨公司",temperature="18^oC"))

print("{0:.5}".format(1.732456))

remote="偏僻的,久遠的"
far="remote"
print("{}的意思為{}".format(remote,far,(remote,far)))

str="{0}*{1}={2}"
c=56
b="10"
print(str.format(c,b,c**int(b)))

print("{0:5}房租為{1:_^15}".format("Yuke",25000))
print("{0:5}房租為{1:>15}".format("YoYo",78000))
print("{0:5}房租為{1:@<15}".format("PiPi",15000))

print("英聽","閱讀","總成績")
print("%s,%1.2f,%1.2f,%d"%("Alice",47.5,65.8,50))
print("%s,%1.2f,%1.2f,%d"%("William",78.6,88.6,96))
print("%s.%1.2f,%1.2f,%d"%("Owan",36.3,10.6,20))

print("{listen},{read},{score}".format(listen="45",read="89",score="65"))
