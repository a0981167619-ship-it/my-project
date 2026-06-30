nums1=[1,3,5,7,9]#5是中間值
aim=int(input("請輸入一個數字:"))
left=0
right=len(nums1)-1
while left<=right:
    m=(left+right)//2
    if nums1[m]>aim:
        right=left-1
        print('此數字為:%d'%(nums1[m]))
        c=nums1.index(nums1[m])
        print('此數字索引位置為:',c)
    else:
        left=m+1
        if aim==7:
            continue
        print('此數字為:',nums1[m])
        c=nums1.index[m]
        print('此數字的索引位置為:',c)
        
       



        

        
 
    