import tkinter as tk
from tkinter import messagebox
computer=tk.Tk()
computer.title('電腦組裝零件選擇器')
label=tk.Label(computer,text='電腦組裝零件選擇',font=('標楷體',36))
label.pack()

assemble=tk.StringVar()
memory=tk.StringVar()

CPU1=tk.Radiobutton(computer,value='i5',text='i5',variable=assemble)
CPU1.pack()

CPU2=tk.Radiobutton(computer,text='i7',value='i7',variable=assemble)
CPU2.pack()

CPU3=tk.Radiobutton(computer,text='i9',value='i9',variable=assemble)
CPU3.pack()

def select():
    selection=assemble.get()
    if selection=='':
        messagebox.showwarning('電腦組裝零件選擇','請至少選擇一個CPU')
    else:
        messagebox.showinfo('電腦組裝零件選擇',selection)

button=tk.Button(computer,text='選擇CPU',command=select)
button.pack()

memory1=tk.Radiobutton(computer,value='8GB',text='8GB',variable=memory)
memory1.pack()

memory2=tk.Radiobutton(computer,text='16GB',value='16GB',variable=memory)
memory2.pack()

memory3=tk.Radiobutton(computer,text='32GB',value='32GB',variable=memory)
memory3.pack()

def memorable():
    container=memory.get()
    if container=='':
        messagebox.showwarning('電腦組裝零件選擇','請至少選擇一個記憶體')
    else:
        messagebox.showinfo('電腦組裝零件選擇',container)

b=tk.Button(computer,text='選擇記憶體',command=memorable)
b.pack()

computer.mainloop()
