import tkinter as tk
comedy=tk.Tk()
label1=tk.Label(text='狀態:等待',font=('新細明體',15))
label1.pack()

var=tk.StringVar()

label2=tk.Label(comedy,textvariable=var)
label2.pack()

def can():
    var.set('狀態:開始')
tk.Button(comedy,command=can,text='check').pack()
def word():
    var.set('狀態:完成')

tk.Button(comedy,text='check',command=word).pack()
comedy.mainloop()




