from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import sys
from datetime import timedelta
from datetime import date
from Resource import count
import os
py = sys.executable


class Lib(Tk):
    def __init__(self):
        super().__init__()

        self.a = IntVar()
        self.b = IntVar()
        self.c = IntVar()

        self.d = StringVar()
        self.e = StringVar()
        self.f = StringVar()

        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        def issue():
            if (len(self.pass_text.get()) == 0) and (len(self.label_5.get()) == 0):
                messagebox.showinfo("Fields cannot be empty")

            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='libMang',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()
                    id = self.label_5.get()
                    d = self.label_6.get()
                    stname = self.user_text.get()
                    strolno = self.pass_text.get()
                    cursor.execute('SELECT Book_avail FROM Books WHERE Book_id = %s ', (id,))
                    pc = cursor.fetchone()
                    print(pc[0])
                    z = int(d)
                    if (pc[0] == "Y"):
                        date_1 = date.today()
                        end_date = date_1 + timedelta(days=z)
                        sql = "INSERT INTO Iss (stname, Strolno, Issue_date, Due_date, Book_id) VALUES (%s, %s, %s, %s, %s)"
                        val = (stname, strolno, date_1, end_date, id)
                        cursor = conn.cursor()
                        cursor.execute(sql, val)
                        conn.commit()

                        count.decount(id,1)

                        messagebox.showinfo('Information', 'Added Sucessfully')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                        self.label_5.delete(0, END)
                    else:
                        messagebox.showinfo('Error', "Book Not Available")

                except Error:

                    messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")
            self.destroy()
            print("GGs")

        def check():
            self.label = Label(self, text="LOGIN", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
            self.label.place(x=550, y=90)
            self.label1 = Label(self, text="Student Name", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label1.place(x=340, y=180)
            self.user_text = Entry(self, textvariable=self.d, width=45)
            self.user_text.place(x=540, y=190)
            self.label2 = Label(self, text="Student RollNo", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label2.place(x=340, y=250)
            self.pass_text = Entry(self, textvariable=self.a, width=45)
            self.pass_text.place(x=540, y=260)

            self.label4 = Label(self, text="Book Name", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label4.place(x=340, y=310)
            self.label_4 = Entry(self, textvariable=self.e, width=45)
            self.label_4.place(x=540, y=320)
            self.label5 = Label(self, text="Book Id", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label5.place(x=340, y=370)
            self.label_5 = Entry(self, textvariable=self.b, width=45)
            self.label_5.place(x=540, y=380)
            self.label6 = Label(self, text="No of days \nyou want to Borrow book ", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label6.place(x=260, y=430)
            self.label_6 = Entry(self, textvariable=self.c, width=45)
            self.label_6.place(x=540, y=440)


            self.butt = Button(self, text="Issue", bg='white', font=10, width=8,command=issue ).place(x=560, y=560)

            self.label3 = Label(self, text="ENTER STUDENT DETAILS", bg='gray', fg='black',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=400, y=30)



        check()

Lib().mainloop()
