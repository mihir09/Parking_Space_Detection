import yaml
from motion_detector import MotionDetector
import mysql.connector
from flask import Flask, render_template, flash, redirect, request, session, url_for, Response
from new_slots import read_name
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegisterForm
from forms1 import FeedbackForm
from werkzeug.security import generate_password_hash, check_password_hash
from checknp import check_np
from sms import send_sms

app = Flask(__name__)
db = mysql.connector.connect()
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/mysqldb'.format(user='root',
                                                                                                    password='root',
                                                                                                    host='localhost',
                                                                                                    database='mysqldb')

app.config['SQLALCHEMY_BINDS'] = {
    'slots': 'sqlite:///slots.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
mn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='mysqldb',
)
db = SQLAlchemy(app)
mycursor = mn.cursor()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256), unique=True)


class Slot(db.Model):
    __bind_key__ = 'slots'
    sno = db.Column(db.Integer)
    slot_name = db.Column(db.String(50), nullable=False, primary_key=True)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.slot_name}"


class FeedBack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256), unique=True)
    number = db.Column(db.String(15), unique=True)
    subject = db.Column(db.String(15), unique=True)
    description = db.Column(db.String(15), unique=True)


class Number1(db.Model):
    np = db.Column(db.String(250), primary_key=True)
    number = db.Column(db.String(250), unique=True)


@app.route('/check_number/', methods=['GET', 'POST'])
def num():
    if request.method == "POST":
        n_p = check_np()
        new_user = Number1(
            np=n_p,
            number='9016291149')

        db.session.add(new_user)
        db.session.commit()

        mycursor.execute("SELECT * FROM Number1")

        for x, y in mycursor:
            if n_p == x:
                send_sms(y)

        return redirect('/')


@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm(request.form)

    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = FeedBack(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            number=form.number.data,
            subject=form.subject.data,
            description=form.description.data
        )

        db.session.add(new_user)
        db.session.commit()

        flash('You have successfully enter data', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        slot_name = request.form['slot_name']

        if read_name(slot_name) == 'success':
            slot = Slot(slot_name=slot_name)
            db.session.add(slot)
            db.session.commit()
    all_slot = Slot.query.all()
    return render_template('index.html', all_slot=all_slot)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate:
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                flash('You have successfully logged in.', "success")
                session['logged_in'] = True
                session['email'] = user.email
                session['username'] = user.username
                return redirect(url_for('index'))
            else:
                flash('Username or Password Incorrect', "Danger")
                return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():

        hashed_password = generate_password_hash(form.password.data, method='sha256')

        new_user = User(
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('You have successfully registered', 'success')
        return redirect(url_for('login'))
    else:
        return render_template('register.html', form=form)


@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))


def gen(name):
    data_file = 'data/' + name + '.yml'
    start_frame = '1'
    video_file = 'videos/' + name + '.mp4'

    with open(data_file, "r") as data:
        points = yaml.load(data, Loader=yaml.FullLoader)
        detector = MotionDetector(video_file, points, int(start_frame))
        detector.detect_motion()


@app.route("/video_feed/<int:sno>", methods=["GET", "POST"])
def video_feed(sno):
    slot_ = Slot.query.filter_by(sno=sno).first()
    name = slot_.slot_name
    Response(gen(name))
    return redirect('/')


@app.route('/delete/<int:sno>')
def delete(sno):
    slot = Slot.query.filter_by(sno=sno).first()
    db.session.delete(slot)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    app.run(host='127.0.1.0', debug=True)
