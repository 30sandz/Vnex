from flask import Flask, render_template,redirect,url_for,request,flash,session
import os
import sqlite3 

app = Flask(__name__)

app.secret_key = "sandeep"
con=sqlite3.connect("image.db")
con.execute("create table if not exists image(pid integer primary key,img TEXT,topic TEXT,name TEXT,sub TEXT,std TEXT)")
con.close()

app.config['UPLOAD_FOLDER']="static\img"
users = {'sandeep':'sandeep0','sandz':'sandz0'}

@app.route("/")
def home():
    return render_template('index.html', title="Vnex")


@app.route("/login")
def log():
    return render_template('login.html', title="Login")

@app.route("/notes", methods=['POST' ,'GET'])
def img():
    con = sqlite3.connect("image.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from image")
    data = cur.fetchall()
    con.close()
    return render_template('images.html', data=data, title="Notes")

@app.route('/admin_page',methods=['POST' ,'GET'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        con = sqlite3.connect("image.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from login where username=? and password=?" ,(username,password))
        data = cur.fetchone()

        if data:
            session["username"]=data["username"]
            session["password"]=data["password"]
            return render_template('admin.html')
        
    return render_template('login.html')
@app.route('/upload', methods=['GET', 'POST'])
def uploadimg():
    if request.method == 'POST':
        upload_image = request.files['upload_image']
        std = request.form.get("std")
        sub = request.form.get("sub")
        name = request.form['name']
        topic = request.form['topic']
         
        if upload_image.filename != '':
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], upload_image.filename)
            upload_image.save(filepath)
            con = sqlite3.connect("image.db")
            cur = con.cursor()
            cur.execute("insert into image(img,topic,name,std,sub)values(?,?,?,?,?)", (upload_image.filename,topic,name,std,sub))
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
    app.run()