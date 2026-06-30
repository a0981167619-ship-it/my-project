"""二維陣列與二階行列式的宣告"""
print("|x1 y1|")
print("|x2,y2|")
E=[[]*2 for i in range(2)]#建立陣列
E=[[0,0],[0,0]]
E[0][0]=int(input("請輸入x1:"))
E[0][1]=int(input("請輸入y1:")) #輸入對應的值
E[1][0]=int(input("請輸入x2:"))
E[1][1]=int(input("請輸入y2:"))
answer=(E[0][0]*E[1][1])-(E[0][1]*E[1][0])#交叉相乘,在相減
print("|%d %d|"%(E[0][0],E[0][1])) #印出陣列
print("|%d %d|"%(E[1][0],E[1][1]))
print("ans:",answer)#答案

print("|x1 y1|")
print("|x2,y2|")
E=[[]*2 for i in range(2)]#建立陣列
E=[[0,0],[0,0]]
E[0][0]=float(input("請輸入x1:"))
E[0][1]=float(input("請輸入y1:")) #輸入對應的值
E[1][0]=float(input("請輸入x2:"))
E[1][1]=float(input("請輸入y2:"))
answer=(E[0][0]*E[1][1])-(E[0][1]*E[1][0])#交叉相乘,在相減
print("|%d %d|"%(E[0][0],E[0][1])) #印出陣列
print("|%d %d|"%(E[1][0],E[1][1]))
print("ans:",answer)#答案


