"""返回已匯入的模組名"""
import sys
print('模組名有:',sys.modules.keys())

c="sys" in sys.modules #查詢sys是否已有記錄在sys.modules中
print(c)

print('返回已匯入模組使用途徑:',sys.modules.values())

import turtle
b= 'turtle' in sys.modules
print(b)

patient= 1 in sys.modules
print(b)