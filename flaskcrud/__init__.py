from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///chasua.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Employee5(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.CHAR(30))
    username = db.Column(db.CHAR(30))
    email = db.Column(db.CHAR(100))
    tel = db.Column(db.CHAR(200))

    def __init__(self, position, username, email, tel):
        self.position = position
        self.username = username
        self.email = email
        self.tel = tel
    

@app.route('/')
def index():
    all_data = Employee5.query.order_by(Employee5.userid.desc()).all() # select * from employee4
    return render_template("index.html", employee5=all_data)

@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        position = request.form["position"]
        username = request.form["username"]
        email = request.form["email"]
        tel = request.form["tel"]

        insertUser = Employee5(position, username, email, tel)
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
    delUser =  Employee5.query.get(uid) #select * from employee2 where userid=3
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        updateUser = Employee5.query.get(request.form.get('userid'))
        updateUser.position = request.form["position"]
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/search', methods=["POST"])
def search():
    textSearch = request.form["textSearch"]
    searchUser= Employee5.query.filter(Employee5.username.contains(textSearch))
    return render_template("index.html", employee5=searchUser, textSearch=textSearch)