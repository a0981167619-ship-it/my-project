'''1.置中標題+四角標籤'''
import tkinter as tk
dff=tk.Tk()
label=tk.Label(text='主畫面',fg='#1A237E',bg="#DAFF08",padx=200,pady=100,font=('',60)).place(relx=0.5,rely=0.5,anchor='center')
label1=tk.Label(text='左上',fg='#BA68CB',bg='#81C784',padx=100,pady=70,font=('',30)).place(relx=0,rely=0,anchor='nw')
label2=tk.Label(text='右上',fg="#C3E4BB",bg='#90CAF9',padx=100,pady=70,font=('',30)).place(relx=1,rely=0,anchor='ne')
label3=tk.Label(text='右下',fg='#AED581',bg='#7986CB',padx=100,pady=70,font=('',30)).place(relx=1,rely=1,anchor='se')
label4=tk.Label(text='左下',fg='#1BFE20',bg='#880E4F',padx=100,pady=70,font=('',30)).place(relx=0,rely=1,anchor='sw')
dff.mainloop()

'''2.三個資訊框(比例定位)'''
text='name=Han \n lucky number= 7 \n food:sandwich'
label5=tk.Label(bg='#FFF176',fg='#F57F17',height=5,width=20,text=text,font=('',30),pady=10).place(relx=0.5,rely=0.5,anchor='n')
word='name=Lyly \n lucky number= 77 \n food:pasta'
label6=tk.Label(bg='#FF8A65',fg='#BF360C',height=5,width=20,text=word,font=('',30),pady=10).place(relx=0.5,rely=0.5,anchor='center')
spell='name=Bonny \n lucky number=6 \n food:ice cream'
label7=tk.Label(bg='#4DD0E1',fg='#006064',text=spell,height=5,width=20,font=('',30),pady=10).place(relx=0.5,rely=0.5,anchor='s')
dff.mainloop()