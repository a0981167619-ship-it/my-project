"""1.整數排序-由小到大排序"""
nums1=[12,7,9,3,15,2]
for i in range(len(nums1)-1):#進行元素-1次
    for a in range(len(nums1)-1-i):#扣掉外層迴圈已排序好的
        if nums1[a]>nums1[a+1]:#如果前面元素>後面元素
            nums1[a],nums1[a+1]=nums1[a+1],nums1[a]#換位置
print("排序後的結果為:",nums1)

"""2.負數與正數混合排序"""
nums2=[4,-2,0,7,-5,3]
for a in range(len(nums2)-1):
    for k in range(len(nums2)-1-a):
        if nums2[k]>nums2[k+1]:
            nums2[k],nums2[k+1]=nums2[k+1],nums2[k]
        print("排序後的結果為",nums2)

"""3.已經部分排序的序列"""
nums3=[1,3,2,5,4,6]
for a in range(len(nums3)-1):
    for i in range(len(nums3)-1-a):
        if nums3[a]>nums3[a+1]:
            nums3[a],nums3[a+1]=nums3[a+1],nums3[a]
            print("排序後的結果為:",nums3)


        

