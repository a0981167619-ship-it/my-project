file=open('ab+ --ex.bin','ab+')
file.write(b'primary')#寫入之後游標會在最後
file.seek(0)#回到開頭
important=file.read()
print(important)

file.write(b'\nfrequence')
file.seek(0)
main=file.read()
print(main)
file.close()
