from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sys
import mysql.connector
from mysql.connector import Error
py = sys.executable

conn = mysql.connector.connect(host='localhost', database='libMang', user='root', password='')
cursor = conn.cursor()

query = "SELECT Book_name FROM Books"
cursor.execute(query)
result = cursor.fetchall()
final_result = [list(i) for i in result]

lst=[]

for i in range(len(final_result)):
    lst.append(final_result[i][0])
print(lst)

root = Tk()

root.maxsize(1200, 700)
root.minsize(400, 400)
root.configure(bg="gray")


def show():
    if root.clicked.get() == "Your Choice" or root.clicked.get() == "Select your Choice":
        messagebox.showinfo(" INVALID Entry")
    else:
        try:
            my_w = tk.Tk()
            my_w.geometry("400x250")

            user=root.clicked.get()
            z = cursor.execute('SELECT * FROM Books where Book_name = %s', (user,))
            print(z)

            e = Label(my_w, width=10, text='id', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=0)
            e = Label(my_w, width=10, text='Name', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
            e.grid(row=0, column=1)
            e = Label(my_w, width=10, text='Count', borderwidth=2, relief='ridge', anchor='w', bg='yellow')
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


            label.config(text=root.clicked.get(), width=30,height=2)
            label.place(x=100,y=200)

            root.mainloop()

        except Error:
            messagebox.showinfo('Error', "Something Goes Wrong,Try restarting")



root.clicked = StringVar()
root.clicked.set("Select your Choice")

drop = OptionMenu(root, root.clicked, *lst)
drop.config(width=35,height=2)
drop.pack(side=BOTTOM,fill=BOTH)
drop.place(x=100,y=75)

button = Button(root, text="Search", command=show)
button.place(x=100, y=145)

label = Label(root, text="Your Choice", bg='gray', fg='black', font=("courier-new", 10))
label.place(x=100, y=200)



root.mainloop()


