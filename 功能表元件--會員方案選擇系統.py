'''會員方案選擇系統'''
import tkinter as tk
from tkinter import messagebox

member=tk.Tk()
member.title('會員方案選擇系統')#設置標題
menu=tk.Menu(member)
member.config(menu=menu)

case=tk.Menu(menu,tearoff=0)
menu.add_cascade(label='會員方案',menu=case)

VIP=tk.StringVar()#把使用者的選擇存起來
def member_case():
    messagebox.showinfo('會員方案',VIP.get())

case.add_radiobutton(label='免費會員',value='免費會員',variable=VIP,command=member_case)
case.add_radiobutton(label='一般會員',value='一般會員',variable=VIP,command=member_case)   #建立選擇
case.add_radiobutton(label='VIP會員',value='VIP會員',variable=VIP,command=member_case)
case.add_radiobutton(label='白金會員',value='白金會員',variable=VIP,command=member_case)

member.mainloop()

