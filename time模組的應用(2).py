'''咖啡店訂餐時間分配系統'''
import time
#時間為:2026-07-10 08:15:00
'''使用strptime將時間轉為struct_time'''
f=time.strptime('2026-07-10 08:15:00','%Y-%m-%d %H:%M:%S')
print('訂餐時間為:',f)

#取得現在時間
foolish=time.localtime()
print('現在時間為:',foolish)

#輸出訂單的三種格式
compress=time.strftime('2026年7月10日 08時15分')
print('訂單時間為:',compress)
print('訂單時間為:',time.asctime())
print('訂單時間為:',time.gmtime())