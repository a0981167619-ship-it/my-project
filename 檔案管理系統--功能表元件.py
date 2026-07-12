import tkinter as tk
from tkinter import messagebox

file=tk.Tk()
file.title('檔案管理系統')

menu=tk.Menu(file)#功能表
file.config(menu=menu)

record=tk.Menu(menu,tearoff=0)#把分隔線拿除
menu.add_cascade(label='檔案',menu=record)#新增主功能表元件

r1=tk.IntVar()
r2=tk.IntVar()
r3=tk.IntVar()
r4=tk.IntVar()

def add():
    if r1.get()==1:#使用者有勾選
        messagebox.showinfo('檔案管理系統','新增檔案')
    else:
        messagebox.showinfo('檔案管理系統','新增檔案功能關閉')

record.add_checkbutton(label='新增檔案',variable=r1,command=add)

def open():
    if r2.get()==1:
        messagebox.showinfo('檔案管理系統','修改檔案')
    else:
        messagebox.showinfo('檔案管理系統','關閉檔案')

record.add_checkbutton(label='開啟檔案',variable=r2,command=open)

def store():
    if r3.get()==1:
        messagebox.showinfo('檔案管理系統','儲存檔案')
    else:
        messagebox.showinfo('檔案管理系統','檔案不儲存')

record.add_checkbutton(label='儲存檔案',variable=r3,command=store)

def program():
    if r4.get()==1:
        messagebox.showinfo('檔案管理系統','關閉程式')
    else:
        messagebox.showinfo('檔案管理系統','開啟程式')

record.add_checkbutton(label='關閉程式',command=program,variable=r4)

file.mainloop()