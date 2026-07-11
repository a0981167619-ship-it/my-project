import tkinter as tk
from tkinter import messagebox

hero=tk.Tk()
hero.title('遊戲英雄選擇器')

label=tk.Label(hero,text='遊戲英雄選擇',font=('標楷體',36))
label.pack()

dict=tk.StringVar()

hero1=tk.Radiobutton(hero,text='戰士',value='戰士',variable=dict)
hero1.pack()

hero2=tk.Radiobutton(hero,text='法師',value='法師',variable=dict)
hero2.pack()

hero3=tk.Radiobutton(hero,text='射手',value='射手',variable=dict)
hero3.pack()

hero4=tk.Radiobutton(hero,text='打野',value='打野',variable=dict)
hero4.pack()

hero5=tk.Radiobutton(hero,text='輔助',value='輔助',variable=dict)
hero5.pack()

def brave():
    brave1=dict.get()
    if dict.get()=='':
        messagebox.showwarning('遊戲英雄選擇系統','請選擇一個位置的英雄')
    else:
        messagebox.showinfo('遊戲英雄選擇系統',brave1)

button=tk.Button(hero,text='英雄選擇',command=brave)
button.pack()

hero.mainloop()
    