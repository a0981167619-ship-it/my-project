import tkinter as tk
resist=tk.Tk()

var=tk.StringVar()
label=tk.Label(resist,textvariable=var)
label.pack()

var.set('Hallo world')#設置
var.get()#讀取

resist.mainloop()