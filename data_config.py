import sqlite3 as sq
con=sq.connect("flask.db")
cur=con.cursor()
# cur.execute("create table register(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(10),email varchar(10),password int,contact varchar(10))")
cur.execute("INSERT INTO register(name,email,password,contact) VALUES(?,?,?,?)", ("gaju", "gaju123@gmail.com", "12345", "1234567890"))

con.commit()
con.close()