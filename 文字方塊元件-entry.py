import tkinter as tk
folder=tk.Tk()
'''show應用'''
folder.title('保密資料')
label=tk.Label(folder,text='請輸入資料內容')
label.pack()
entry=tk.Entry(folder,width=30,bg='black',fg='brown',show='$')#用show隱藏密碼內容
entry.pack()


'''銀行PIN碼驗證'''

folder.title('銀行PIN碼驗證')
label1=tk.Label(folder,text='請輸入4位數的PIN碼')
label1.pack()
entry_PIN=tk.Entry(folder,width=50,bg='#E0F7FA',fg='black',show='⚝')
entry_PIN.pack()

'''state'''
entry_input=tk.Entry(folder,state='normal')#使用者可輸入的狀態
entry_input.pack()
entry_output=tk.Entry(folder,state='disabled')#使用者無法輸入
entry_output.pack()
entry1=tk.Entry(folder,state='readonly')#使用者只能查看結果,不可輸入
entry1.pack()

var=tk.StringVar()
entry=tk.Entry(folder,textvariable=var)
entry.pack()
label=tk.Label(folder,textvariable=var)
label.pack()
folder.mainloop()