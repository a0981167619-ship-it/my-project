def total_sleep(hours_list):
    total=0
    for i in hours_list:#遍歷整個清單
        total+=i
    return total#算總睡眠數
def average_sleep(hours_list):
    total=total_sleep(hours_list)
    average=total/len(hours_list)
    return average#計算平均睡眠時數
