"""最快到達的捷運站"""
nums2=[3,5,7,10,15]
left=0
right=len(nums2)-1
T=int(input("請輸入一個整數:"))
while left<=right:
    medium=(left+right)//2
    if nums2[medium]<=T:
        left=medium+1
        if nums2[medium]<=6:
            print('最符合你的條件是:',nums2[medium])
            c=nums2.index(nums2[medium])
            print('索引位置為:',c)
        
    else:
        right=medium-1
        print('最符合你的條件是:',nums2[medium])
        c=nums2.index(nums2[medium])
        print('此數字的索引位置為:',c)
        
                 

       
