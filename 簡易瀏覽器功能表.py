'''簡易瀏覽器功能表'''
import tkinter as tk
from tkinter import messagebox
easy=tk.Tk()
easy.title('簡易瀏覽器功能表')
menu=tk.Menu(easy)#建立功能表元件
easy.config(menu=menu)

file=tk.Menu(menu,tearoff=0)#把底線拿除
menu.add_cascade(label='檔案',menu=file)

add=tk.IntVar()

def add_file():
    if add.get():
        messagebox.showinfo('新增','新增分頁')
    else:
        messagebox.showinfo('新增','關閉分頁')

file.add_checkbutton(variable=add,label='新增分頁',command=add_file,)

easy.mainloop()
