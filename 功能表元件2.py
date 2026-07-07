'''功能表--範例'''
import tkinter as tk
type=tk.Tk()

menu=tk.Menu(type)
type.config(menu=menu)

line=tk.Menu(menu,tearoff=0)
menu.add('cascade',label='底線',menu=line)
line.add('command',label='底線選擇')

type.mainloop()