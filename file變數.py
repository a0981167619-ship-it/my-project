file=open('rectangle.py',mode='w')
print('檔名:',file.name)#查看檔名
print('模式:',file.mode)#查看開啟檔案的定義模式
print('檔案關閉狀態:',file.closed)#查看檔案的開啟狀態

file2=open('三角形.py',mode='r')
print("{0}為{1}".format('檔名',file2.name))
print('{0}為{1}'.format('定義模式',file2.mode))
print('{0}為{1}'.format('檔案關閉狀態',file2.closed))