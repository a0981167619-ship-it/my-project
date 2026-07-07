'''checkbutton--範例'''
import tkinter as tk
from tkinter import messagebox
sacrifice=tk.Tk()
menu=tk.Menu(sacrifice)

sacrifice.config(menu=menu)

view=tk.Menu(menu,tearoff=0)#把分隔線拿除
menu.add_cascade(label='影像',menu=view)

vision=tk.IntVar()

def invision():#使用者點了過後,會發生的事
    if vision.get():
        messagebox.showinfo('view','白色影像已開啟')
    else:
        messagebox.showinfo('view','白色影像未開啟')

view.add_checkbutton(variable=vision,command=invision,label='白色影像')

sacrifice.mainloop()
