"""與對齊格式有關方法"""
h="What's up?"
print("原字串:",h)
print("字串置中:",h.center(20))
print("字串置中,符號填補:",h.center(20,"☺"))
print("字串置左,符號填補:",h.ljust(20,"❤"))
print("字串置右,符號填補:",h.rjust(20,"⚝"))
f="y=ax+b"
print("字串左側補0:",f.zfill(100))
print("字串分3部分:",f.partition("*"))
y="ax/bx/c"
print("以/分割字串:",y.splitlines(True))#保留分割字元
print("以/分割字串:",y.splitlines(False))#去除分割字元
