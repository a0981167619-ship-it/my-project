import os
c=os.getcwd()
print("目前路徑為",c)#取得當前路徑
deceitful=os.listdir("D:\程式\_pycache2_\PythonApplication1\my python design")
print(deceitful)#列出指定路徑之下的所有檔案
sincere=os.walk("D:\程式\_pycache2_\PythonApplication1\my python design",False)#以遞迴方式搜尋指定路徑下的所有子目錄以及檔案
print(sincere)
insincere=os.mkdir(r"C:\line")#建立資料夾
os.rmdir(r"C:\line")#刪除資料夾
treacherous=os.mkdir(r"C:\123456")
os.rmdir(r"C:\123456")
