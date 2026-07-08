'''銀行帳戶資訊界面'''
import tkinter as tk
bank=tk.Tk()
bank.title('銀行帳戶資訊界面')
bank.geometry('500x300')#設定視窗大小

label=tk.Label(text='帳戶資訊',font=('微軟正黑體',38))

label.pack(anchor='n')#位置定為正上方中間

label1=tk.Label(text='姓名: Hank',font=('微軟正黑體',20))
label1.pack(anchor='w')#將位置定為左方中間

label2=tk.Label(text='帳號: InformationK12345678.gmail.com',font=('微軟正黑體',20))
label2.pack(pady=20,anchor='w')

label3=tk.Label(text='目前餘額: 25000元',font=('微軟正黑體',20),fg="#0775F3")
label3.pack(anchor='e')#將位置定為右方中間

label4=tk.Label(text='本月支出: 8000元',font=('微軟正黑體',20),fg='red')
label4.pack(pady=10,anchor='e')

label5=tk.Label(text='帳戶狀態: 正常',font=('微軟正黑體',20))
label5.pack(anchor='s')#將位置定為下方中間

bank.mainloop()


