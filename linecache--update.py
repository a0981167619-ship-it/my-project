import linecache
file=linecache.getline('file.py',2)#返回檔案的第2行內容
print(file)

file1=linecache.updatecache('file.py')
print(file1)#更新緩存區數據