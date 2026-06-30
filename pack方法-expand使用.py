'''pack-expand方法的使用'''
import tkinter as tk
gentle=tk.Tk()
label=tk.Label(bg='#7CFC00',padx=15,pady=20)
label.pack(fill=tk.X,expand=True)#向水平方向間距拉伸
gentle.mainloop()

label=tk.Label(bg='#6A5ACD',pady=50)
label.pack(fill=tk.Y,expand=False)#label只占自己需要的空間
gentle.mainloop()

label=tk.Label(bg='#C0C0C0',pady=50,padx=890)
label.pack()
gentle.mainloop()