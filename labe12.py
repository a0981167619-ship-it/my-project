import tkinter as tk
finish=tk.Tk()
text='I \n am \n sad '
label2=tk.Label(finish,text=text, justify='left')
label2.pack()
finish.mainloop()

text='I \n am \n not \n happy \n because \n I \n effort \n score \n but \n as \n lower \n as'
label=tk.Label(fg='black',text=text,justify='right')
label.pack()
finish.mainloop()

img=tk.PhotoImage(file='"D:\c11\au.png.png"')
label=tk.Label(finish, image=img)
label.pack(padx=10,pady=10)
finish.mainloop()