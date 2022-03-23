from tkinter import *
import sys
import os
py = sys.executable



class Lib(Tk):
    def __init__(self):
        super().__init__()

        self.minsize(1200, 750)
        self.configure(bg="gray")
        self.title("LIBRARY MANAGEMENT SYSTEM")

        def find():
            os.system('%s %s' % (py, 'find.py'))
        def Issue():
            os.system('%s %s' % (py, 'issue.py'))
        def lst():
            os.system('%s %s' % (py, 'lst.py'))
        def add():
            os.system('%s %s' % (py, 'add.py'))
        def ret():
            os.system('%s %s' % (py, 'ret.py'))
        def isstable():
            os.system('%s %s' % (py, 'isstable.py'))




        def check():
            self.label = Label(self, text="Your Choice ", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
            self.label.place(x=550, y=90)

            self.butt1 = Button(self, text="Find Book", bg='white', font=16, width=20, command=find).place(x=540, y=180)

            self.butt2 = Button(self, text="Issue Book", bg='white', font=16, width=20, command=Issue).place(x=540, y=280)

            self.butt3 = Button(self, text="Book List", bg='white', font=16, width=20, command=lst).place(x=540, y=380)

            self.butt4 = Button(self, text="Add Book", bg='white', font=16, width=20, command=add).place(x=540, y=680)

            self.butt5 = Button(self, text="Return Book", bg='white', font=16, width=20, command=ret).place(x=540, y=580)

            self.butt6 = Button(self, text="Issued Book List", bg='white', font=16, width=20, command=isstable).place(x=540,
                                                                                                            y=480)


            self.label3 = Label(self, text="WELCOME TO LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black',
                                font=("courier-new", 24, 'bold'))
            self.label3.place(x=260, y=30)

        check()


Lib().mainloop()
