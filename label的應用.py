'''三種顏色文字label'''
import tkinter as tk
saded=tk.Tk()
text='strike \n struggle \n sting'
label=tk.Label(text=text,fg='#4169E1',bg='black',justify='left')#justify使文字靠左對齊
label.pack()
saded.mainloop()

text='opinion \n vidg \n finish'
label=tk.Label(text=text,fg='#B0C4DE',bg='#FFD700',justify='right')
label.pack()
saded.mainloop()

text='unique \n different \n billion '
label=tk.Label(text=text,fg='#98FF98',bg='#32CD32',justify='center')
label.pack()
saded.mainloop()