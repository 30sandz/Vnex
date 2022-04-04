from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/admin")
def add():
    return render_template('admin.html')

@app.route("/login")
def log():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()