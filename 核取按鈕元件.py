'''範例'''
import tkinter as tk
prominent=tk.Tk()
prominent.title('Checkbutton')#設置標題

var=tk.IntVar()

check=tk.Checkbutton(prominent,text='分數',variable=var,onvalue=100,offvalue=0)#設置onvalue: 有勾選成績為100分, offvalue: 沒勾選成績為0分
check.pack()

def check_open():
    print(var.get())#查看成績

button=tk.Button(prominent,text='查看成績',command=check_open)
button.pack()

prominent.mainloop()