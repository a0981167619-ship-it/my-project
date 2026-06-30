"""檢查模組是否在sys.modules中"""
import sys
fame=123 in sys.modules
print(fame)

concern='123' in sys.modules
print(concern)

silly='os.path' in sys.modules
print(silly)
