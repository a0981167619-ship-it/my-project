'''成績判斷系統'''
import tkinter as tk
from tkinter import messagebox

witness=tk.Tk()
witness.title('成績判斷系統')
score=72

def exam_rule():
    if score>=60:
        messagebox.showinfo('校務系統','及格')
    else:
        messagebox.showwarning('校務系統','不及格')

button=tk.Button(witness,text='成績判斷',command=exam_rule)
button.pack()

witness.mainloop()