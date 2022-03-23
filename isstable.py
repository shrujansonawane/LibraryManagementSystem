import mysql.connector
import tkinter  as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("900x300")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="libMang"
)
my_conn = my_connect.cursor()
####### end of connection ####

my_conn.execute("SELECT * FROM iss")
e=Label(my_w,width=15,text='Student_Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Student_RollNo',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='Issued_Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='Due_Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text='Return_Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=4)
e=Label(my_w,width=10,text='Book_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
e.grid(row=0,column=5)
i=1
for student in my_conn:
    for j in range(len(student)):
        e = Label(my_w,width=20, text=student[j], fg='black')
        e.grid(row=i, column=j)
        #e.insert(END, student[j])
    i = i + 1
    
my_w.mainloop()

