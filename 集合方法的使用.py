"""集合方法的使用"""
#ex.社團喜好調查
musicClub={"class A","class C","class D","class F"}
spotClub={"class B","class C","class D","class E"}

m=musicClub.difference(spotClub)
print("差集為:",m)#取兩者的差集(只參加musicClub,沒有參加spotClub社的人)

M=spotClub.difference(musicClub)
print("差集為:",M)##取兩者的差集(只參加spotClub,沒有參加musicClub社的人)

n=musicClub.intersection(spotClub)
print(n)#取兩者的交集(同時參加musicClub社與spotClub社的人)

N=musicClub.union(spotClub)
print(N)#取兩者的聯集,有參加任何一個社團的所有班級,有重複也只取一次

a=musicClub.symmetric_difference(spotClub)
print(a)#取兩者的對稱差集,只參加一個社團的班級

#ex.選修課程名單
artClass={"Class A","Class B","Class E","Class G"}
scienceClass={"Class B","Class C","Class E","Class F"}

x=artClass.difference(scienceClass)
print(x)
y=scienceClass.difference(artClass)
print(y)

z=artClass.intersection(scienceClass)
print(z)

X=artClass.union(scienceClass)
print(X)

Y=scienceClass.symmetric_difference(artClass)
print(Y)


