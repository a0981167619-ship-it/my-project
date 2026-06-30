import sys

if len(sys.argv)<0:
    print("尚未取得外部參數值")
else:
    print('Python版本號:',sys.version)
    print('作業系統:',sys.platform)

    for i in range(len(sys.argv)):
        print('param:'+str(i),sys.argv[i])