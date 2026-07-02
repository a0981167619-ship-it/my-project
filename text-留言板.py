'''留言板'''
def message():
    text4.insert(tk.END,entry.get()+'\n')

word='留言板:'
text4=tk.Text(victory,borderwidth=30,height=10)
text4.insert('1.0',word)
text4.pack()

entry=tk.Entry(victory)
entry.pack()

but=tk.Button(victory,text='送出留言',command=message)
but.pack()
victory.mainloop()