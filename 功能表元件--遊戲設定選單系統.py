'''遊戲設定選單系統'''
import tkinter as tk
from tkinter import messagebox

game=tk.Tk()
game.title('遊戲設定選單系統')#設置標題
menu=tk.Menu(game)
game.config(menu=menu)

setting=tk.Menu(menu,tearoff=0)#把分隔線拿除
menu.add_cascade(label='設定',menu=setting)#新增主功能表元件

'''建立三個有關此主功能表的函式'''
voice=tk.IntVar()
def open_voice():#音效
    if voice.get()==1:#有勾為1,沒勾為0
        messagebox.showinfo('音效','音效已開啟')

    else:
        messagebox.showinfo('音效','靜音模式')

setting.add_checkbutton(label='開啟音效',variable=voice,command=open_voice)#建立checkbutton

store_file=tk.IntVar()
def file():
    if store_file.get()==1:
        messagebox.showinfo('檔案','已儲存')
    else:
        messagebox.showinfo('檔案','尚未儲存')

setting.add_checkbutton(label='自動存檔',command=file,variable=store_file)
demonstrate=tk.IntVar()

def key():
    if demonstrate.get()==1:
        messagebox.showinfo('進階功能','顯示提示已開啟')
    else:
        messagebox.showinfo('進階功能','顯示提示已關閉')
setting.add_checkbutton(label='顯示提示',variable=demonstrate,command=key)

game.mainloop()