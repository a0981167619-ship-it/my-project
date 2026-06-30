import tkinter as tk
forbid=tk.Tk()
text='I \n was \n childhood \n is so bad'
label=tk.Label(bg='#20B2AA',padx=100,pady=200,text=text,justify='center')
label.pack(side=tk.LEFT)#將標籤擺在左邊
forbid.mainloop()

label=tk.Label(bg='#FF7F50',padx=50,pady=40)
label.pack(side=tk.BOTTOM)#將標籤擺在底部
forbid.mainloop()

label=tk.Label(bg="#EC8ACC",padx=80,pady=90)
label.pack(side=tk.TOP)
forbid.mainloop()#將標籤擺在上方

label=tk.Label(bg='#4B0082',pady=100)
label.pack(side=tk.RIGHT)#將標籤擺在右邊
forbid.mainloop()