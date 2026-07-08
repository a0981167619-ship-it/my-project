'''公告欄介面'''
import tkinter as tk
announce=tk.Tk()
announce.title('公告欄介面')#設置標題
announce.geometry('400x300')#設置視窗大小

label1=tk.Label(text='學校公告',font=('標楷體',38))
label1.pack(side='top',fill='both',expand=True)
label2=tk.Label(text='1.明天正常上課',font=('標楷體',20),fg='blue')
label2.pack(pady=20)
label3=tk.Label(text='2.請穿著合宜的服裝',font=('標楷體',20),fg='blue')
label3.pack(pady=20)
label4=tk.Label(text='3.請攜帶餐盒、文具、書本',font=('標楷體',20),fg='blue')
label4.pack(pady=20)

label5=tk.Label(text='請準時到校',font=('標楷體',30),fg='red')
label5.pack(expand=True,side='bottom')
announce.mainloop()