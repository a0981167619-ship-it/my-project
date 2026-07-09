'''留言編輯'''
import tkinter as tk
message=tk.Tk()
message.title('留言編輯器')
message.geometry('500x350')

text=tk.Text(message,borderwidth=3,wrap='char',highlightbackground='#456321',highlightcolor="#BB8EDA",highlightthickness=2)#文字自動換行
text.pack()

text.insert(tk.END,'請輸入你的留言:')
def input():
    text.config(state='disabled')#使用者不可編輯

button=tk.Button(message,text='鎖定留言',command=input)
button.pack()

def output():
    text.config(state='normal')#使用者可編輯

button1=tk.Button(message,command=output,text='重新編輯')
button1.pack()

message.mainloop()
