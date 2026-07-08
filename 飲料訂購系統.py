'''飲料點餐介面'''
import tkinter as tk
drink=tk.Tk()
drink.title('飲料訂購系統')#設置標題

label=tk.Label(text='歡迎光臨',font=('標楷體',40))
label.pack(pady=25,side='top')

label1=tk.Label(text='紅茶',font=('標楷體',20))
label1.pack(side='left')

label2=tk.Label(text='奶茶',font=('標楷體',20))
label2.pack(pady=10,side='left')

label3=tk.Label(text='綠茶',font=('標楷體',20))
label3.pack(pady=10,side='left')



drink.mainloop()

