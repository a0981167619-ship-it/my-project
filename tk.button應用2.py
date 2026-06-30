import tkinter as tk
tragic=tk.Tk()
var=tk.StringVar()

label1=tk.Label(tragic,text='未按下')
label1.pack()

def joy():
    var.set('已按下')

label3=tk.Label(tragic,textvariable=var)
label3.pack()
tk.Button(tragic,command=joy,text='check').pack()
tragic.mainloop()