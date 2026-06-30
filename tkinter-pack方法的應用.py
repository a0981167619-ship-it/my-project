'''example'''
import tkinter as tk
female=tk.Tk()
BMI=tk.Button(female,height=30,width=20,text='BMI值')
BMI.pack(side=tk.TOP)

weight=tk.Button(female,height=30,width=20,text='體重值')
weight.pack(side=tk.TOP)

female.mainloop()

'''網站版面配置'''
label=tk.Label(bg='#6495ED',text='我的網站',padx=90,pady=100)
label.pack(side=tk.TOP)

text='entertainment \n quiet room \n bookstore'
label1=tk.Label(bg="#C8EC8F",text=text,padx=80,pady=60,font=('',45))
label1.pack(side=tk.LEFT)

text='歡迎來到我的網站'
label=tk.Label(bg="#0F67B9",text=text,padx=500,pady=300,font=('新細明體',50))
label.pack()
female.mainloop()
