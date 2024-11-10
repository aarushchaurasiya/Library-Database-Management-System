import sqlite3

def connecting():
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(ID integer PRIMARY KEY,title text , author text , year integer , book integer)")
    con.commit()
    con.close()

def inserting(title,author,year,book):
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute(" INSERT INTO books VALUES(null,?,?,?,?)",(title,author,year,book))
    con.commit()
    con.close()

def printing():
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    content = cur.fetchall()
    con.close()
    return content


def searching(title="",author="",year="",book=""):
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR book=?",(title,author,year,book))
    content = cur.fetchall()
    con.close()
    return content


def deleting(id):
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE ID=? " ,(id,))
    con.commit()
    con.close()

def updaitng(id,title,author,year,book):
    con = sqlite3.connect("list_of_books.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title=?,author=?,year=?,book=? WHERE id=?",(title,author,year,book,id))
    con.commit()
    con.close()

# connecting()
# inserting("cormen","DAA ",2022 ,9876)
# # print(searching(year=2021))
# # deleting(3)
# print(printing())