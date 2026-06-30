for i in range(1,10):
    print(i)
    for j in range(1,10): #外圈去控制內圈
        print(j)
        print("{0}×{1}={2:^2}".format(i,j,i*j),end="     ") #format輸出
        
        
