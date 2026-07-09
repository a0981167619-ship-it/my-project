'''公告閱讀器'''
import tkinter as tk
read=tk.Tk()
read.title('公告閱讀器')
read.geometry('500x350')

text=tk.Text(read,font=('標楷體',20),fg='red',borderwidth=5,wrap='char',highlightbackground="#FF8398",highlightthickness=2,highlightcolor='green')#設置邊框寬度為5,會自動換行
text.pack()

text.insert(tk.END,'【重要通知】' \
'下週一進行校園環境檢查,請同學保持教室整潔')

text.config(state='disabled')#使用者不可修改內容
read.mainloop()



