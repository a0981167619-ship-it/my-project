'''餐廳訂位查詢系統'''
import tkinter as tk
site=tk.Tk()
site.title('餐廳訂位查詢系統')
site.geometry('450x300')

label=tk.Label(text='餐廳訂位查詢系統',font=('微軟正黑體',36))
label.pack(side='top')

label1=tk.Label(text='餐廳名稱:',font=('微軟正黑體',20))
label1.pack(anchor='n')#將位置定為上方中間

name=tk.Entry(site)
name.pack()

result=tk.Label(site,font=('微軟正黑體',20))
result.pack()

def restaurant():
    name1=name.get()
    result.config(text='餐廳名稱:'+name1)

button=tk.Button(text='查詢',command=restaurant)
button.pack()

site.mainloop()