import mysql.connector
import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("400x250")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="libMang"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM books")
e=Label(my_w,width=10,text='id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='No',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Available',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
i=1
for student in my_conn:
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, student[j])
    i=i+1
my_w.mainloop()
