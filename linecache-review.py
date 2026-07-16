import linecache
a=linecache.getlines('傳址呼叫.py')
print(a)#得到此檔案的全部內容

b=linecache.getlines('time模組.py')
print(b)

ambition=linecache.getline('Max.py',2)#返回此檔案的第2行內容
print(ambition)

choke=linecache.getline('moonnight.py',5)#返回此檔案的第5行內容
print(choke)

linecache.clearcache()#清除緩存

linecache.checkcache('[linecache--checkcache.2py]')#檢查緩存區數據並更新
linecache.updatecache('linecache--checkcache2.py')#更新緩存區數據


