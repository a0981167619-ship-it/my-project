#字串方法""
a="high \height \nlong"
print(a.split())#以空格與換行符號分割

b="refuse \neplace \nrecycle"
print(b.split())

c="king \tkingdom \tweapon"
print(c.split())

"""
搜尋特定字串出現次數""
"""
x="Hallo world cpp"
x1=x.count("p")
x2=x.count("Hallo",0,15)
print("{}\n (p)出現{}次,(Hallo)出現{}次".format(x,x1,x2))

y="fish fish fish fish fish"
y1=y.count("f",0)#從0開始索引
y2=y.count("ish",1,10)#從1-10開始索引
print("{}\n (f)出現{}次, (ish)出現{}次".format(y,y1,y2))#\v

z="harm harmful wound world wisdom weapon somehow"
z1=z.count("w",0,70)#從0-70開始索引
z2=z.count("m",6)#從6開始索引
print("{}\n (w)出現{}次,(m)出現{}次".format(z,z1,z2))
