# -*- coding: utf-8 -*-
<<<<<<< HEAD
from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shindalsoo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(50))

    def __init__(self, username, email, tel):
        self.username = username
        self.email = email
        self.tel = tel

@app.route('/')
def index():
    all_data = Employee.query.order_by(Employee.userid.desc()).all() # select * from employee
    return render_template("index.html", employees=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        tel = request.form['tel']

        insertUser = Employee(username,email,tel)
=======
from gtts import gTTS
from playsound import playsound
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
>>>>>>> 276194b0f326570254eb189621afa45c243708e7
        db.session.add(insertUser)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/delete/<uid>')
def delete(uid):
<<<<<<< HEAD
    delUser = Employee.query.get(uid) # select * from Employee where userid=3
=======
    delUser =  Employee5.query.get(uid) #select * from employee2 where userid=3
>>>>>>> 276194b0f326570254eb189621afa45c243708e7
    db.session.delete(delUser)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
<<<<<<< HEAD
        updateUser = Employee.query.get(request.form.get('userid'))
=======
        updateUser = Employee5.query.get(request.form.get('userid'))
        updateUser.position = request.form["position"]
>>>>>>> 276194b0f326570254eb189621afa45c243708e7
        updateUser.username = request.form['username']
        updateUser.email = request.form['email']
        updateUser.tel = request.form['tel']
        db.session.commit()
        return redirect(url_for('index'))

<<<<<<< HEAD
@app.route('/search', methods=['POST'])
def search():
    txtsearch = request.form['txtsearch']
    searchUser = Employee.query.filter(Employee.username.contains(txtsearch))
    return render_template("index.html", employees=searchUser, txtsearch=txtsearch)

@app.route('/playmp3')
def playmp3():
    text = "오늘은, 2020년 8월 20일입니다. 고양이가 소리를 내려고합니다. 우리모두 스마트고양이를 응원합시다~~람쥐"
    filename = "hellosmartcat.mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)
    playsound(filename)

    return "고양이가 소리를 냈습니다."
=======
@app.route('/search', methods=["POST"])
def search():
    textSearch = request.form["textSearch"]
    searchUser= Employee5.query.filter(Employee5.username.contains(textSearch))
    return render_template("index.html", employee5=searchUser, textSearch=textSearch)

@app.route('/playmp3')
def playmp3():
    text = "고양이가 소리를 내려고 합니다 우리 모두 스마트 고양이를 주문합시다"
    filename = "hellocat.mp3"
    tts = gTTS(text=text, lang="ko")
    tts.save(filename)
    playsound(filename)
    return "소리를 냈습니다"
>>>>>>> 276194b0f326570254eb189621afa45c243708e7
