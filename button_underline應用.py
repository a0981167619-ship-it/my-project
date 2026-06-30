import tkinter as tk
trendy=tk.Tk()
label1=tk.Label(text='點擊按鈕')
label1.pack()
def high():
    tk.Button(trendy,underline=0,text='check').pack()
tk.Button(trendy,command=high,text='check').pack()
trendy.mainloop()