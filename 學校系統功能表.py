'''學校系統功能表'''
import tkinter as tk
from tkinter import messagebox
school=tk.Tk()
school.title('學校系統功能表')

m=tk.Menu(school)
school.config(menu=m)

student=tk.Menu(m,tearoff=0)#把分隔線拿除
m.add_cascade(label='學生',menu=student)#新增主功能表元件

material=tk.IntVar()

def check():
    if material.get():
        messagebox.showinfo('資料','查看資料')
    else:
        messagebox.showinfo('資料','關閉資料')

student.add_checkbutton(label='查看資料',command=check,variable=material)#新增次功能表元件

revise=tk.IntVar()

def modify():
    if revise.get():
        messagebox.showinfo('資料修改系統','修改資料')
    else:
        messagebox.showinfo('資料修改系統','資料內容保留不更動')

student.add_checkbutton(label='修改資料',command=modify,variable=revise)

sign=tk.IntVar()

def out():
    if sign.get():
        messagebox.showinfo('登入系統','登出')
    else:
        messagebox.showinfo('登入系統','登入')

student.add_checkbutton(label='登出',command=out,variable=sign)

course=tk.Menu(m,tearoff=0)
m.add_cascade(label='課程',menu=course)#新增主功能表元件

select=tk.IntVar()

def class1():
    if select.get():
        messagebox.showinfo('選課系統','選課')
    else:
        messagebox.showinfo('選課系統','取消選課')

course.add_checkbutton(label='選課',command=class1,variable=select)

examine=tk.IntVar()

def curriculum():
    if examine.get():
        messagebox.showinfo('課表','查看課表')
    else:
        messagebox.showinfo('課表','關閉課表查詢')

course.add_checkbutton(label='查看課表',variable=examine,command=curriculum)

score=tk.IntVar()

def fraction():
    if score.get():
        messagebox.showinfo('成績查詢系統','成績查詢')
    else:
        messagebox.showinfo('成績查詢系統','關閉當前頁面')

course.add_checkbutton(label='成績查詢',command=fraction,variable=score)

system=tk.Menu(m,tearoff=0)
m.add_cascade(label='系統',menu=system)

system1=tk.IntVar()

def system2():
    if system1.get():
        messagebox.showinfo('系統設定','關於學校系統')
    else:
        messagebox.showinfo('系統設定','關閉學校系統')

system.add_checkbutton(label='關於系統',command=system2,variable=system1)

leave=tk.IntVar()

def depart():
    if leave.get():
        messagebox.showinfo('學校網頁','離開')
    else:
        messagebox.showinfo('學校網頁','進入')

system.add_checkbutton(label='離開',command=depart,variable=leave)

school.mainloop()