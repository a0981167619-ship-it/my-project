'''線上考試提交系統'''
import tkinter as tk
from tkinter import messagebox

exam=tk.Tk()
exam.title('線上考試提交系統')

label=tk.Label(exam,text='線上考試提交系統',font=('標楷體',30))
label.pack()

def hand_in():
    handin=messagebox.askyesno('考試提交確認','是否確定提交考卷?')

    if handin==True:
        messagebox.showinfo('考試提交確認','考卷提交成功!')
    if handin==True:
            messagebox.showinfo('考卷提交確認系統','考卷已經提交,無法再次修改')
    else:
        messagebox.showinfo('考卷提交確認','已取消提交')

   

button=tk.Button(exam,text='提交考卷',command=hand_in)
button.pack()
exam.mainloop()    
