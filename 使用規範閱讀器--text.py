'''使用規範閱讀器'''
import tkinter as tk
rule=tk.Tk()
rule.title('使用規範閱讀器')
rule.geometry('500x350')

text=tk.Text(rule,borderwidth=4,wrap='char',fg="#011481",font=('標楷體',20),highlightbackground='gray',highlightthickness=2,highlightcolor='black')#會自動換行、外框背景顏色為灰色
text.pack()

text.insert(tk.END,'【使用規範】\n 1.請勿在系統中輸入不當內容 \n 2.使用完畢後請記得登出帳號 \n 3.請遵守平台使用規則')

text.config(state='disabled')#使用者不可修改內容

rule.mainloop()
