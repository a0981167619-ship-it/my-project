"""18.循序搜尋法"""
"""找第一個等於目標值的偶數"""
nums1=[3,4,6,4,5]
target=int(input("請輸入一個數字:"))
discovery=False
for i in range(len(nums1)):
    if nums1[i]==target:
        if i%2==0:
            discovery=True
        print(i)
        break

"""計算有幾個數字大於平均值"""
nums2=[2,4,6,8]
average=(2+4+6+8)/4
print('平均值為%d'%(average))

for i in range(len(nums2)):
    count=0
    if nums2[i]>average:
        print(i)
        break
    count+=i
    print('有%d個數字大於平均值'%(count))

    