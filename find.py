from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sys
import os
import mysql.connector
from mysql.connector import Error
py = sys.executable



class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = IntVar()
        self.b = StringVar()
        self.c = IntVar()
        self.maxsize(1200, 700)
        self.minsize(1200, 700)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        def trial():
            self.destroy()
            os.system('%s %s' % (py, 'trila.py'))

        def find():
            if len(self.book_id.get()) == 0 & len(self.book_name.get()) == 0:
                messagebox.showinfo(" INVALID Entry")
            elif len(self.book_name.get()) > 20:
                messagebox.showinfo("Book Name too long")
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',
                                                   database='libMang',
                                                   user='root',
                                                   password='')
                    cursor = conn.cursor()

                    user = self.book_name.get()
                    print(user)
                    iid = self.book_id.get()
                    print(iid)
                    z = cursor.execute('SELECT * FROM Books where Book_name = %s', (user,))
                    print(z)

                    my_w = tk.Tk()
                    my_w.geometry("400x250")

                    e = Label(my_w, width=10, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                    e.grid(row=0, column=0)
                    e = Label(my_w, width=10, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                    e.grid(row=0, column=1)
                    e = Label(my_w, width=10, text='No', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                    e.grid(row=0, column=2)
                    e = Label(my_w, width=10, text='Available', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
                    e.grid(row=0, column=3)
                    i = 1
                    for student in cursor:
                        for j in range(len(student)):
                            e = Entry(my_w, width=10, fg='blue')
                            e.grid(row=i, column=j)
                            e.insert(END, student[j])
                        i = i + 1
                    self.mainloop()



                except Error:
                    messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")
            print("GGs")
        

        def check():
            self.label1 = Label(self, text="Book ID", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label1.place(x=370, y=180)
            self.label1a = Label(self, text="(Plz enter integer value)", bg='gray', fg='black',
                                 font=("courier-new", 10))
            self.label1a.place(x=370, y=220)
            self.book_id = Entry(self, textvariable=self.a, width=45)
            self.book_id.place(x=370, y=260)

            self.label2 = Label(self, text="Book Name", bg='gray', fg='black', font=("courier-new", 18, 'bold'))
            self.label2.place(x=370, y=300)
            self.label1b = Label(self, text="(Plz enter String value)", bg='gray', fg='black', font=("courier-new", 10))
            self.label1b.place(x=370, y=340)
            self.book_name = Entry(self, textvariable=self.b, width=45)
            self.book_name.place(x=370, y=380)

            self.butt = Button(self, text="Find Book", bg='white', font=10, width=8, command=find ).place(x=480, y=450)

            self.label5 = Label(self, text="If you Dont Remember the Book ID Click Here", bg='gray', fg='black', font=("courier-new", 18))
            self.label5.place(x=200, y=550)
            self.butt1 = Button(self, text="Find with Book Name", bg='white', font=10, width=20, command=trial).place(x=410, y=600)

            self.label3 = Label(self, text="Please Fill Details of Books", bg='gray', fg='black',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=260, y=30)

        check()


Lib().mainloop()
