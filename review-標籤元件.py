import tkinter as tk
sad=tk.Tk()
label=tk.Label(sad,height=1600)
label=tk.Label(sad,width=900)
text='disguish'
label=tk.Label(text=text,font=('微軟正黑體',20),fg='#E6E6FA',bg='#808000',padx=20,pady=20 ,bd=50)
label.pack()
sad.mainloop()

text='kill \n minup \n can \n'
label=tk.Label(text=text,fg='#00CED1',justify='center',font=('新細明體',100))
label.pack()
sad.mainloop()

'''多行文字練習'''
label=tk.Label(height=1600,width=900)
text='anoisy \n vividy \n moon'
label=tk.Label(text=text,font=('標楷體',30),justify='left',fg='black')#文字靠左對齊
label.pack()
sad.mainloop()
text='123 \n 456 \n 789'
label=tk.Label(text=text,justify='right')#文字靠右對齊
label.pack()
sad.mainloop()
text='*** \n === \n %%%'
label=tk.Label(text=text,justify='center')#文字靠中對齊
label.pack()
sad.mainloop()