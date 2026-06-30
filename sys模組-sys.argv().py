import sys
print('全部參數:',sys.argv)

if len(sys.argv)>1:
    print("第二個參數:",sys.argv[2])
else:
    print('沒有參數傳入')
