'''密碼驗證系統'''
import tkinter as tk
from tkinter import messagebox

assure=tk.Tk()
assure.title('密碼驗證系統')

correct_password='1234'
user_password='1234'

def secret():
    if user_password=='':
        messagebox.showwarning('密碼驗證','請輸入密碼')

    elif user_password==correct_password:
        messagebox.showinfo('密碼驗證','登入成功')

    else:
        messagebox.showerror('密碼驗證','密碼錯誤')

B=tk.Button(assure,text='密碼驗證',command=secret)
B.pack()

assure.mainloop()