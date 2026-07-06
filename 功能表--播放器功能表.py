'''播放器功能表--範例2'''
import tkinter as tk
record=tk.Tk()

menu=tk.Menu(record)
record.config(menu=menu)#將功能表加到視窗

record_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='播放',menu=record_menu)#新增主功能表元件
record_menu.add_command(label='播放')
record_menu.add_command(label='暫停') #新增次功能表元件
record_menu.add_command(label='停止')

record_list=tk.Menu(menu,tearoff=0)#將分隔線拿除
menu.add_cascade(label='播放清單',menu=record_list)
record_list.add_command(label='新增歌曲')
record_list.add_command(label='刪除歌曲')

presentation=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='說明',menu=presentation)
presentation.add_command(label='關於播放器')
record.mainloop()