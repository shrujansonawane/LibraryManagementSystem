from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import sys
from Resource import count


class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = IntVar()
        self.c = IntVar()
        self.b = StringVar()

        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")


        def ADD():
            if len(self.user_ID.get()) == 0:
                messagebox.showinfo(" INVALID Entry")
            elif len(self.user_name.get()) > 20:
                messagebox.showinfo("Book Name too long")
            else:
                try:

                    conn = mysql.connector.connect(host='localhost',
                                                   database='libMang',
                                                   user='root',
                                                   password='')
                    #hasvalue = 'false'
                    cursor = conn.cursor()
                    user = self.user_name.get()
                    print(user)
                    iid = self.user_ID.get()
                    print(iid)
                    cont = self.user_count.get()
                    print(cont)
                    z=cursor.execute('SELECT Book_name FROM Books where Book_name = %s LIMIT 1', (user,))
                    print(z)
                    self.user_ID.delete(0, END)
                    self.user_name.delete(0, END)
                    self.user_count.delete(0, END)

                    if cursor.fetchone():
                        count.count(user,cont)
                    else:
                        cursor = conn.cursor(buffered = True)
                        print(iid, cont)
                        sql = "INSERT INTO Books (Book_id, Book_name, Book_count, Book_avail) VALUES (%s, %s, %s, %s)"
                        val = (iid, user, cont, "Y")
                        cursor.execute(sql, val)
                        conn.commit()
                        messagebox.showinfo('Information', 'Added Sucessfully')
                        self.user_ID.delete(0, END)
                        self.user_name.delete(0, END)
                        self.user_count.delete(0, END)
                except Error:
                    messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")
            self.destroy()
            print("GGs")




        def check():
            self.label1 = Label(self, text="Book ID", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label1.place(x=370, y=180)
            self.label1a = Label(self, text="(Plz enter integer value)", bg='gray', fg='black', font=("courier-new", 10))
            self.label1a.place(x=370, y=220)
            self.user_ID = Entry(self, textvariable=self.a, width=45)
            self.user_ID.place(x=370, y=260)


            self.label2 = Label(self, text="Book Name", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label2.place(x=370, y=300)
            self.label1b = Label(self, text="(Plz enter String value)", bg='gray', fg='black',font=("courier-new", 10))
            self.label1b.place(x=370, y=340)
            self.user_name = Entry(self, textvariable=self.b, width=45)
            self.user_name.place(x=370, y=380)

            self.label1 = Label(self, text="Total No of Books", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label1.place(x=370, y=420)
            self.label1c = Label(self, text="(Plz enter integer value)", bg='gray', fg='black',font=("courier-new", 10))
            self.label1c.place(x=370, y=460)
            self.user_count = Entry(self, textvariable=self.c, width=45)
            self.user_count.place(x=370, y=500)

            self.butt = Button(self, text="Add Book", bg='white', font=10, width=8, command=ADD).place(x=480, y=570)


            self.label3 = Label(self, text="Please Fill Details of Books", bg='gray', fg='black',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=260, y=30)

        check()

Lib().mainloop()
