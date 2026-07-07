'''簡易記事本功能系統'''
import tkinter as tk
from tkinter import messagebox

note=tk.Tk()
note.title('簡易記事本功能系統')#設置標題
menu=tk.Menu(note)
note.config(menu=menu)

file=tk.Menu(menu,tearoff=0)#將分隔線拿除
menu.add_cascade(label='設定',menu=file)
file.add_command(label='新增檔案')
file.add_command(label='開啟檔案')
file.add_command(label='儲存檔案')
file.add_separator()
file.add_command(label='離開程式')

note.mainloop()
