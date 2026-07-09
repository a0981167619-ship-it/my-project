'''電影訂票查詢'''
import tkinter as tk
movie=tk.Tk()
movie.title('電影訂票查詢')
movie.geometry('450x250')

label1=tk.Label(text='電影訂票查詢',font=('微軟正黑體',36))
label1.pack(side='top')

label=tk.Label(text='電影名稱:',font=('微軟正黑體',20))
label.pack(anchor='n')#將label放於上方中間

entry_movie=tk.Entry(movie)
entry_movie.pack()

result=tk.Label(movie,font=('微軟正黑體',20))
result.pack()

def movie1():
    movie=entry_movie.get()
    result.config(text='你查詢的電影為:'+movie)

button=tk.Button(text='查詢',command=movie1)
button.pack()

movie.mainloop()
    

