'''功能表元件--範例'''
import tkinter as tk
chase=tk.Tk()
menu=tk.Menu(chase)#建立功能表列
chase.config(menu=menu)

select_menu=tk.Menu(menu)
menu.add_cascade(label='選擇',menu=select_menu)#新增主功能表項目

run_menu=tk.Menu(menu,tearoff=0)#將參數設為0,可將分隔線移除
menu.add_cascade(label='執行',menu=run_menu)
run_menu.add_command(label='執行Python')#以按鈕形式新增子功能表項目

help_menu=tk.Menu(menu)
menu.add_cascade(label='幫忙',menu=help_menu)

file_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='檔案',menu=file_menu)
file_menu.add_command(label='檔案列表:')

chase.mainloop()
