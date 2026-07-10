'''密碼規則說明系統'''
import tkinter as tk
code=tk.Tk()
code.title('密碼規則說明系統')

label=tk.Label(text='密碼規則說明系統',font=('標楷體',30),fg='blue')
label.pack()

s=tk.Scrollbar(code,orient='horizontal')#設定為水平捲軸

t=tk.Text(code,xscrollcommand=s.set,highlightbackground="#ADFFB8",highlightthickness=5,wrap='none')

s.config(command=t.xview)

s.pack(side='bottom',fill='x')
t.pack(fill='both',expand=True,side='left')

def password():
    for i in range(50):
        t.insert(tk.END,'密碼規則：密碼長度必須至少八個字元，並且需要包含英文大小寫、數字以及特殊符號，請勿使用個人容易猜測的資訊作為密碼。')

button=tk.Button(code,text='explain',command=password)
button.pack()

code.mainloop()