import tkinter as tk
sad=tk.Tk()

def aware():
    print('math')

tk.Button(sad,command=aware,text='math').pack()

def award():
    print('English')
tk.Button(sad,command=award,text='English').pack()

sad.mainloop()


