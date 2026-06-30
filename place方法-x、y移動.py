import tkinter as tk
gun=tk.Tk()
label=tk.Label(bg='#DC143C',width=50,height=30).place(x=0,y=0)
gun.mainloop()

label2=tk.Label(bg='#006400',width=20,height=60).place(x=-90,y=-60)#往左90像素,往上60像素
label3=tk.Label(bg='#6495ED',width=10,height=70,text='A').place(x=70,y=10)#往右70像素,往下10像素
gun.mainloop()

text='I am so tired'
label4=tk.Label(bg='#87CEEB',width=200,height=600,fg='#00008B',text=text).place(relx=0,rely=0)#將標籤往左、往上
gun.mainloop()

label45=tk.Label(text='continuous',fg='#FFB6C1',bg='#8B0000',padx=50,pady=100).place(relx=0.5,rely=0.5)#將標籤置中
gun.mainloop()

label6=tk.Label(text='speak out',fg='#98FB98',bg='#006400',width=2000,height=900).place(relx=1,rely=1)#將標籤往右、往下移
gun.mainloop()