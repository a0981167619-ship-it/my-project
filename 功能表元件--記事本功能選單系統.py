'''記事本功能選單系統'''
import tkinter as tk
note=tk.Tk()

menu=tk.Menu(note)
note.config(menu=menu)
note.title('記事本功能選單系統')

file_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='檔案',menu=file_menu)#新增主功能表項目
file_menu.add_command(label='新增檔案')#新增次功能表項目
file_menu.add_command(label='開啟檔案')
file_menu.add_command(label='儲存檔案')

edit_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='編輯',menu=edit_menu)
edit_menu.add_command(label='復原')
edit_menu.add_command(label='重做')
edit_menu.add_command(label='全選')

explain_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='說明',menu=explain_menu)
explain_menu.add_command(label='關於')
explain_menu.add_command(label='使用說明')

note.mainloop()
