import tkinter as tk
from tkinter import messagebox

store=tk.Tk()
store.title('遊戲存檔確認系統')

label=tk.Label(store,text='存檔確認系統',font=('標楷體',20),fg='red')
label.pack()
def game():
     q=messagebox.askyesno('存檔確認','是否要覆蓋目前存檔?')

     if q==True:
          messagebox.showinfo('存檔確認','存檔成功')

     else:
          messagebox.showinfo('存檔確認','存檔失敗')

button=tk.Button(store,command=game,text='存檔確認')
button.pack()

store.mainloop()
