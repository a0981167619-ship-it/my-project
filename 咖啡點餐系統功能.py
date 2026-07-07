'''咖啡點餐系統功能'''
import tkinter as tk
coffee=tk.Tk()
coffee.title('咖啡點餐系統功能')

menu=tk.Menu(coffee)
coffee.config(menu=menu)

check=tk.Menu(menu,tearoff=0)#將分隔線拿除
menu.add('cascade',label='點餐',menu=check)#新增主功能表元件
check.add('command',label='點拿鐵')
check.add('command',label='點美式')
check.add('command',label='點卡布奇諾')                            #新增次功能表元件
check.add('command',label='-----------------------------')
check.add('command',label='查看價格')

coffee_system=tk.Menu(menu,tearoff=0)
menu.add('cascade',label='系統',menu=coffee_system)
coffee_system.add('command',label='清空訂單')
coffee_system.add('command',label='重置系統')
coffee_system.add('command',label='離開程式')

explaination=tk.Menu(menu,tearoff=0)
menu.add('cascade',label='說明',menu=explaination)
explaination.add('command',label='使用說明')
explaination.add('command',label='關於本店...')

coffee.mainloop()