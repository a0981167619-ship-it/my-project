import tkinter as tk
winning=tk.Tk()
winning.title('label元件')
label=tk.Label(winning,text='july')
label.pack()
winning.mainloop()

'''簡單天氣顯示器'''
label=tk.Label(text='Taipei city',bg='#ADD8E6',fg='#00008B',justify='center')
label.pack()
label=tk.Label(text='sunny day',bg='#FFFFE0',fg='#FF8C00',justify='center')
label.pack()
label=tk.Label(text='22 Celsius',bg='#FF4500',fg='#FFFFFF')
label.pack()
winning.mainloop()