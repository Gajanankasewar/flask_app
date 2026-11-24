import sqlite3 as sq
from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reg")
def reg():
   return render_template("reg.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/gallary")
def gallary():
    return render_template("gallary.html")

@app.route("/formsave", methods=["GET","POST"])
def formsave():
    if request.method=="POST":
        fn=request.form["name"]
        em=request.form["email"]
        ps=request.form["password"]
        cn=request.form["contact"]

        con=sq.connect("Flask.db")
        cur=con.cursor()
        cur.execute("insert into register(name,email,password,contact)values(?,?,?,?)",[fn,em,ps,cn])

        con.commit()
       
        return "Register Completed Successfully"
    else:
        return "Something Went wrong"

@app.route("/viewdata")
def viewdata():

    con=sq.connect("Flask.db")
    cur=con.cursor()
    data=cur.execute("select * from register order by id desc")
    
    con.commit()

    return render_template("viewdata.html",data=data)

@app.route("/del_data")
def del_data():
    return render_template("delete.html")

@app.route("/delete", methods=["GET","POST"])
def delete():

    if request.method=="POST":
        dl=request.form["deletename"]

        con=sq.connect("flask.db")
        cur=con.cursor()
        cur.execute("delete from register where name=?",(dl,))

        con.commit()

        return "Data deleted Successfully"
    else:
        return "id not found"




if __name__=="__main__":
    app.run(debug=True)


