import tkinter as tk
dominant=tk.Tk()
label1=tk.Label(bg='#90CAF9',text='one',font=('',10),height=5,width=20).grid(column=0,row=0)
label2=tk.Label(bg='#BA68C8',text='two',font=('',10),height=5,width=20).grid(column=0,row=1)
label3=tk.Label(bg='#4DB6AC',text='three',font=('',10),height=5,width=20).grid(column=1,row=0)
label4=tk.Label(bg='#AED581',text='four',font=('',10),height=5,width=20).grid(column=1,row=1)
dominant.mainloop()

'''pady、padx間距'''
label5=tk.Label(bg="#650FE6",padx=5,pady=10,height=12,width=20).place(anchor='nw')#調整水平間距與垂直間距
label6=tk.Label(bg='#4527A0',padx=5,pady=10,height=12,width=20).place(anchor='ne')
dominant.mainloop()

'''columaspan、rowspan 合併數量'''
label7=tk.Label(bg='#2196F3',text='alcohol',height=10,width=20).grid(column=0,row=0,columnspan=2,rowspan=2)#左右、上下各跨兩格
label8=tk.Label(bg='#1E88E5',text='cigarette',height=10,width=20,padx=50,pady=10).grid(column=1,row=0,columnspan=2,rowspan=2)
dominant.mainloop()

'''sticky填滿格子'''
label9=tk.Label(bg='#1A237E',text='distinguished',fg='yellow',padx=10,pady=10).grid(column=0,row=0,sticky='n')#將元件靠上
label10=tk.Label(bg='#311B92',text='extraordinary',fg='pink',padx=10,pady=10).grid(column=1,row=0,sticky='s')#將元件靠下
label11=tk.Label(bg='#827717',text='outstanding',padx=10,pady=10).grid(sticky='e')#將元件靠右
label12=tk.Label(bg='#263238',text='common',fg='#F3E5F5',padx=10,pady=10).grid(sticky='w')#將元件靠左
dominant.mainloop()
