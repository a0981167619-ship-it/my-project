'''遊戲畫質設定系統'''
import tkinter as tk
from tkinter import messagebox

play=tk.Tk()
play.title('遊戲畫質設定系統')#設置標題
menu=tk.Menu(play)

play.config(menu=menu)

set=tk.Menu(menu,tearoff=0)#把分隔線拿除
menu.add_cascade(label='設定',menu=set)

setting=tk.StringVar()#全部選擇共用一個Var

def scenery():
    messagebox.showinfo('畫質',setting.get())#顯示使用者的選擇

set.add_radiobutton(label='低畫質',value='低畫質',variable=setting,command=scenery)
set.add_radiobutton(label='中畫質',value='中畫質',variable=setting,command=scenery)         #建立選擇
set.add_radiobutton(label='高畫質',value='高畫質',variable=setting,command=scenery)
set.add_radiobutton(label='最高畫質',value='最高畫質',variable=setting,command=scenery)

play.mainloop()

