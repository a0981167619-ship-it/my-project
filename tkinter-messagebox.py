'''範例'''
import tkinter as tk
from tkinter import messagebox

fate=tk.Tk()
fate.title('訊息方塊元件')
fate.geometry('50x50')

def show():
    messagebox.showinfo('網站訊息','進入此網站')#使用show只會顯示一個確定紐

def ask():
     messagebox.askyesno('來自本機','是否要打開此文件 ?')#使用ask產生2-3個按鈕來互動

button=tk.Button(fate,text='網站訊息',command=show).pack(side='left',pady=20)
button1=tk.Button(fate,text='詢問使用者意見',command=ask).pack(side='right',pady=20)

fate.mainloop()