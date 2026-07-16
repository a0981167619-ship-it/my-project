import shutil
shutil.copyfile('main.py','main--copy.py') #複製檔案
shutil.copyfile('串列2.py','串列2-copy.py')

shutil.copy2('hearteasy.py','copy-hearteasy.py')#複製有關此檔案的資訊
shutil.copy2('bool布林值.py','bool布林值-copy.py')

'''移動檔案'''
shutil.move('串列2-copy.py','copy檔案')
shutil.move('copy-hearteasy.py','copy檔案')
shutil.move('bool布林值-copy.py','copy檔案')