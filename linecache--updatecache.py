import linecache
linecache.checkcache('test檔.py')

a=linecache.getline('test檔.py',2)
print(a)
b=linecache.updatecache('test檔.py')#更新緩存區數據
print(b)