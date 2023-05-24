from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user
from random import randint
import time
import os


# MY db connection
local_server= True
app = Flask(__name__)
app.secret_key='PrithvirajSawant'


# this is for getting unique user access
login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas__name'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/h20webmonitor'
db=SQLAlchemy(app)

# here we will create db models that is tables
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class records(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    hid=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class report(db.Model):
    username=db.Column(db.String(50))
    email=db.Column(db.String(50))
    pid=db.Column(db.Integer,primary_key=True)
    productname=db.Column(db.String(100))
    productdesc=db.Column(db.String(300))
    # price=db.Column(db.Integer)



class Trig(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fid=db.Column(db.String(100))
    action=db.Column(db.String(100))
    timestamp=db.Column(db.String(100))


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))


    

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/ReportL')
@login_required
def ReportL():
    # query=db.engine.execute(f"SELECT * FROM `report`") 
    query=report.query.all()
    return render_template('ReportL.html',query=query)


# @app.route('/triggers')
# @login_required
# def triggers():
#     # query=db.engine.execute(f"SELECT * FROM `trig`") 
#     query=Trig.query.all()
#     return render_template('triggers.html',query=query)



@app.route('/Aboutus')
def Aboutus():
    # query=db.engine.execute(f"SELECT * FROM `report`") 
    return render_template('Aboutus.html')

@app.route('/ImageProcessing')
@login_required
def ImageProcessing():
    # query=db.engine.execute(f"SELECT * FROM `report`") 
    return render_template('ImageProcessing.html')

@app.route('/MachineLearning')
@login_required
def MachineLearning():
    # query=db.engine.execute(f"SELECT * FROM `report`") 
    return render_template('MachineLearning.html')

@app.route('/livelocation')
@login_required
def livelocation():
    # query=db.engine.execute(f"SELECT * FROM `report`")
    return render_template('livelocation.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        print(username,email,password)
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Succes Please Login","primary")
        return render_template('login.html')

          

    return render_template('signup.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","success")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","danger")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))


@app.route('/test')
def test():
    try:
        Test.query.all()
        return 'My database is Connected'
    except:
        return 'My db is not Connected'


app.run(debug=True)    