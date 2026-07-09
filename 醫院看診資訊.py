'''醫院看診資訊'''
import tkinter as tk
hospital=tk.Tk()
hospital.title('門診資訊')

hospital.geometry('550x350')#設置視窗大小

label=tk.Label(text='門診資訊',font=('標楷體',38))
label.grid(column=2,row=0)#定位為第二欄、第0列

label1=tk.Label(text='姓名:',font=('標楷體',20),fg='blue')
label1.grid(column=0,row=1)#定位為第0欄、第0列

label2=tk.Label(text='Bobo',font=('標楷體',20),fg='blue')
label2.grid(column=1,row=1)#定位為第1欄、第1列

label3=tk.Label(text='科別:',font=('標楷體',20),fg='blue')
label3.grid(column=0,row=2)#定位為第0欄、第二列

label4=tk.Label(text='一般外科',font=('標楷體',20),fg='blue')
label4.grid(column=1,row=2)#定位為第1欄、第2列

label5=tk.Label(text='看診號碼:',font=('標楷體',20),fg='blue')
label5.grid(column=0,row=3)#定位為第0欄、第三列

label6=tk.Label(text='35',font=('標楷體',20),fg='blue')
label6.grid(column=1,row=3)#定位為第1欄、第三列

label7=tk.Label(text='診間:',font=('標楷體',20),fg='blue')
label7.grid(column=0,row=4)#定位為第0欄、第四列

label8=tk.Label(text='201',font=('標楷體',20),fg='blue')
label8.grid(column=1,row=4)#定位為第1欄、第四列

label9=tk.Label(text='請耐心等候叫號',font=('標楷體',20),fg="#87FD59")
label9.grid()

hospital.mainloop()