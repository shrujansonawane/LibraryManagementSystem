from tkinter import *
from tkinter import messagebox
import sys
import os
import mysql.connector
from mysql.connector import Error
py = sys.executable
from datetime import timedelta
from datetime import date
from Resource import count

#creating window
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.c = IntVar()
        self.d = IntVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")


#verifying input
        def chex():
            if (len(self.stname.get()) == 0 and len(self.bname.get()) == 0 and len(self.id_text.get()) == 0 and len(self.bid.get()) == 0):
                messagebox.showinfo(" Field cannot be Empty" )
            elif (len(self.stname.get()) > 50 or len(self.bname.get()) > 50 or len(self.id_text.get()) > 50 or len(self.bid.get()) > 50):
                messagebox.showinfo(" Field too long")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='libMang',
                                         user='root',
                                         password='')
                    cursor = conn.cursor()

                    id = self.id_text.get()
                    nam = self.stname.get()

                    ia = self.bid.get()
                    date_1 = date.today()
                    cursor.execute('UPDATE iss SET 	ret_date = %s where stname = %s AND Strolno = %s AND Book_id= %s ',(date_1, nam, id, ia))
                    conn.commit()

                    count.count(ia, 1)


                    messagebox.showinfo(" Sucessful "," Successfully Returned")
                    self.id_text.delete(0, END)
                except Error:
                    messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")

        def check():


                    self.label = Label(self, text="Return", bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
                    self.label.place(x=550, y=100)
                    self.label1 = Label(self, text="Student Name" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label1.place(x=340, y=180)
                    self.stname = Entry(self, textvariable=self.a, width=45)
                    self.stname.place(x=540, y=190)
                    self.label2 = Label(self, text="Book_Name" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
                    self.label2.place(x=340, y=250)
                    self.bname = Entry(self, textvariable=self.b, width=45)
                    self.bname.place(x=540, y=260)
                    self.label3 = Label(self, text="Roll No", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
                    self.label3.place(x=340, y=320)
                    self.id_text = Entry(self, textvariable=self.c, width=45)
                    self.id_text.place(x=540, y=330)
                    self.label4 = Label(self, text="Book Id", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
                    self.label4.place(x=340, y=390)
                    self.bid = Entry(self, textvariable=self.d, width=45)
                    self.bid.place(x=540, y=400)
                    self.butt = Button(self, text="Return",bg ='white', font=10, width=8, command=chex).place(x=580, y=500)
                    self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
                    self.label3.place(x=350, y=30)


        check()

Lib().mainloop()
