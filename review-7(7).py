"""17.氣泡排序法(由大到小排序)"""
nums1=[4,7,2,5,9]
for i in range(len(nums1)-1):
    for a in range(len(nums1)-1-i):
        if nums1[a]<nums1[a+1]:
            nums1[a],nums1[a+1]=nums1[a+1],nums1[a]
print("排序後的結果為:",nums1)

"""排序後找最大差值"""
nums2=[4,9,1,6]
for i in range(len(nums2)-1):
    for a in range(len(nums2)-1-i):
        if nums2[a]>nums2[a+1]:
            nums2[a],nums2[a+1]=nums2[a+1],nums2[a]
            print("排序後的結果為:",nums2)
            latter=max(nums2)-min(nums2)
            print("最大差值為:",latter)
"""只排序前一半"""
nums3=[8,3,5,1,9,2]
for i in range(len(nums3)-4):
    for a in range(len(nums3)-4-i):
        if nums3[a]>nums3[a+1]:
            nums3[a],nums3[a+1]=nums3[a+1],nums3[a]
            print('排序後的結果為:',nums3)