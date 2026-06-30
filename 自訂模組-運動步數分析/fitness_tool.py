def total_water(water_list):
    total=0
    for i in water_list:#遍歷整個清單
        total+=i
        return total
def average_water(water_list):
    total=total_water(water_list)
    average=total/len(water_list)
    return average
    
    
    
    