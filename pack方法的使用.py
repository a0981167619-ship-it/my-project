'''pack方法'''
import tkinter as tk
hanmory=tk.Tk()
label=tk.Label(bg='#191970',padx=10,pady=20)#設置水平間距為10,垂直間距為20
label.pack()
hanmory.mainloop()
label=tk.Label(bg='#FFFACD',padx=50,pady=20)#設定標籤元件的尺寸
label.pack()
hanmory.mainloop()

label=tk.Label(bg='#4682B4',padx=50,pady=70)
label.pack(fill=tk.BOTH)#用fill填滿水平間距與垂直間距
hanmory.mainloop()

label=tk.Label(bg='#FFF8DC',padx=10)
label.pack(fill=tk.X)#用fill填滿水平間距
hanmory.mainloop()

label=tk.Label(bg='#00BFFF',pady=100)
label.pack(fill=tk.Y)#用fill填滿垂直間距
hanmory.mainloop()

label=tk.Label(bg='#AFEEEE')
label.pack(fill=tk.NONE)#不填滿任何東西
hanmory.mainloop()