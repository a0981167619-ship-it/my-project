'''VIP會員狀態顯示系統'''
import tkinter as tk
roughly=tk.Tk()
roughly.title('VIP會員狀態顯示系統')#設置標題

var=tk.IntVar()
textvariable=tk.StringVar()

def group():
    if var.get()==1:#使用者有勾選
        textvariable.set('VIP會員: 已開通')
    else:#使用者沒有勾選
        textvariable.set('VIP會員: 未開通')

check=tk.Checkbutton(roughly,variable=var,text='VIP會員',bg="#72C8FA",command=group)
check.pack()

label=tk.Label(roughly,textvariable=textvariable)
label.pack()

roughly.mainloop()
