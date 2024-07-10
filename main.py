from  tkinter  import *
import tkinter as tk
from math import *

	
from datetime import date
today = date.today()
window = tk.Tk()
window.title("Age Calculator By Devasya ")
window.geometry("600x500")


title = Label(window,text="Age Calculator By Devasya ")
title.grid(row=0,column=0,columnspan=5,pady=15)

label=Label(window,text="Enter Your Details ")
label.place(x=200,y=50)

birth=Label(window,text=" Birth Month")


birth.grid(row=1,column=0,pady=25)

birth1=Entry(window)
birth1.grid(row=1,column=1)

birth2=Label(window,text="Birth Year ")
birth2.grid(row=2,column=0,pady=5)
birth3=Entry(window)
birth3.grid(row=2,column=1)
birth4=Label(window,text="Birth day ")
birth4.grid(row=3,column=0,pady=5)
birth5=Entry(window)
birth5.grid(row=3,column=1)





today = date.today()
def calculate():
  
  d= int(birth5.get())
  m=int(birth1.get())
  y=int(birth3.get())
  age = today.year-y-((today.month, today.day)<(m,d))
  t1.config(state='normal')
  t1.delete('1.0', tk.END)
  t1.insert(tk.END,age)
  t1.config(state='disabled')
def exit():
    window.destroy()
  
calc=Button(window,text="Calculate",command = calculate)
calc.place(x=150,y=200) 
l3 = tk.Label(window,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="darkgreen",bg="#F7DC6F")
l3.place(x=50,y=250)
t1=tk.Text(window,width=5,height=0,state="disabled")
t1.place(x=290,y=250)
b2=tk.Button(window,text="Exit Application!",font=("Arial",13),command=exit)
b2.place(x=150,y=350)
tk.mainloop()




