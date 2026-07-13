import linecache
clear=linecache.getline('test檔.py',3)#返回此檔案第三行的內容

print(clear)

linecache.clearcache()#清除緩存

clear2=linecache.getline('test檔.py',2)
print(clear2)
linecache.clearcache()