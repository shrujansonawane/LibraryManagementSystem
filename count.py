import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='libMang'
)

def count(inp, u):
    a = "SELECT Book_count FROM Books WHERE Book_id = %s"
    data = (inp,)
    c = mydb.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print(myresult[0], type(u))
    t = myresult[0] + int(u)
    sql = "UPDATE Books SET Book_count = %s where Book_id = %s"
    d = (t, inp)
    c.execute(sql, d)
    mydb.commit()

    c.execute('SELECT Book_avail FROM Books WHERE Book_id = %s ', (inp,))
    pc = c.fetchone()
    print(pc[0])
    if (pc[0] == "N"):
        sq = "UPDATE Books SET Book_avail = %s where Book_id = %s"
        d = ('Y', inp)
        c.execute(sq, d)
        mydb.commit()


def decount(inp, u):
    a = "SELECT Book_count FROM Books WHERE Book_id = %s"
    data = (inp,)
    c = mydb.cursor()
    c.execute(a, data)
    myresult = c.fetchone()
    print(myresult[0], type(u))
    t = myresult[0] - int(u)
    sql = "UPDATE Books SET Book_count = %s where Book_id = %s"
    d = (t, inp)
    c.execute(sql, d)
    mydb.commit()


    c.execute('SELECT Book_count FROM Books WHERE Book_id = %s ', (inp,))
    pc = c.fetchone()
    print(pc[0])
    if (pc[0] == 0):
        sq = "UPDATE Books SET Book_avail = %s where Book_id = %s"
        d = ('N', inp)
        c.execute(sq, d)
        mydb.commit()


