from turtle import title
from webbrowser import get
from flask import Flask, render_template,redirect,url_for,request,flash
import os
import sqlite3

app = Flask(__name__)

app.secret_key = "sandeep"
con=sqlite3.connect("image.db")
con.execute("create table if not exists image(pid integer primary key,img TEXT)")
con.close()

app.config['UPLOAD_FOLDER']="static\img"
users = {'sandeep':'sandeep0','sandz':'sandz0'}

@app.route("/")
def home():
    return render_template('index.html', title="Vnex")

@app.route("/admin")
def add():
    return render_template('admin.html', title="admin")

@app.route("/image")
def img():
    con = sqlite3.connect("image.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from image")
    data = cur.fetchall()
    con.close()
    return render_template('images.html', data=data, title="Data")

@app.route("/login")
def log():
    return render_template('login.html', title="login")

@app.route('/login_page',methods=['POST' ,'GET'])
def admin():
    if request.method == 'POST':
        name = request.form["username"]
        password = request.form["password"]

        if name not in users:
            return render_template('login.html')
            flash('Invalid Username or Password' ,'error')
        else:
            if users[name]!= password:
                return render_template('login.html')
                flash('Invalid Username or Password', 'error')
            else:
                return render_template('admin.html')
                flash('Login successful')
@app.route('/upload', methods=['GET', 'POST'])
def uploadimg():
    con = sqlite3.connect("image.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from image")
    data = cur.fetchall()
    con.close()
    if request.method == 'POST':
        upload_image = request.files['upload_image']

        if upload_image.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
            upload_image.save(filepath)
            con = sqlite3.connect("image.db")
            cur = con.cursor()
            cur.execute("insert into image(img)values(?)", (upload_image.filename, ))
            con.commit()
            flash("file uploaded successfully")

            con = sqlite3.connect("image.db")
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("select * from image")
            data = cur.fetchall()
            con.close()
            return render_template("index.html")
            
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)