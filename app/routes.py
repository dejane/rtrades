from flask import render_template, redirect,url_for, request, flash, jsonify, make_response, abort
from .forms import *
from .models import *
from . import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc
from threading import Thread
from websocket import create_connection
import json


#async decorator
def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper


@async
def get_btc(db, Btctrades):
    ws = create_connection("wss://api2.bitfinex.com:3000/ws")
    #ws.connect("wss://api2.bitfinex.com:3000/ws")
    ws.send(json.dumps({
        "event": "subscribe",
        "channel": "trades",
        "pair": "BTCUSD",
        "prec": "P0"
    }))


    while True:
        result = ws.recv()
        result = json.loads(result)
        #only uses the trade execution messages since they are most recent/accurate
        if len(result) == 6:
            new_trade = Btctrades(channel_id=result[0],msg_type=result[1],trade_id=result[2],timestamp=result[3],price=result[4],amount=result[5], time_recorded=datetime.now())
            db.session.add(new_trade)
            db.session.commit()
        print ("Received '%s'" % result)

@async
def get_eth(db, Ethtrades):
    ws = create_connection("wss://api2.bitfinex.com:3000/ws")
    #ws.connect("wss://api2.bitfinex.com:3000/ws")
    ws.send(json.dumps({
        "event": "subscribe",
        "channel": "trades",
        "pair": "ETHUSD",
        "prec": "P0"
    }))


    while True:
        result = ws.recv()
        result = json.loads(result)
        if len(result) == 6:
            new_trade = Ethtrades(channel_id=result[0],msg_type=result[1],trade_id=result[2],timestamp=result[3],price=result[4],amount=result[5], time_recorded=datetime.now())
            db.session.add(new_trade)
            db.session.commit()
        print ("Received '%s'" % result)



@async
def get_xrp(db, Xrptrades):
    ws = create_connection("wss://api2.bitfinex.com:3000/ws")
    #ws.connect("wss://api2.bitfinex.com:3000/ws")
    ws.send(json.dumps({
        "event": "subscribe",
        "channel": "trades",
        "pair": "XRPUSD",
        "prec": "P0"
    }))


    while True:
        result = ws.recv()
        result = json.loads(result)
        if len(result) == 6:
            new_trade = Xrptrades(channel_id=result[0],msg_type=result[1],trade_id=result[2],timestamp=result[3],price=result[4],amount=result[5], time_recorded=datetime.now())
            db.session.add(new_trade)
            db.session.commit()
        print ("Received '%s'" % result)



get_btc(db, Btctrades)
get_eth(db, Ethtrades)
get_xrp(db, Xrptrades)


#login manager helps in managing users logged in and also logging them out
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(str(user_id))

#landing page
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

#register route
@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            hashed_pass = generate_password_hash(form.password.data, method='pbkdf2:sha256:100000')
            new_user = User(username = form.username.data.lower(), email=form.email.data.lower(),firstname=form.firstname.data, lastname=form.lastname.data, password=hashed_pass, create_date=datetime.now())
            db.session.add(new_user)
            db.session.commit()


            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Username/Email already in use. Please select another set of username/email')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

#login route
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        flash('Your email or password is wrong. Try again')

    return render_template('login.html', form=form)

#The dashboard
@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
    #only called one time on load - then jquery ajax takes over
    rows_btcusd = Btctrades.query.order_by(desc(Btctrades.time_recorded)).limit(30).all()
    rows_ethusd = Ethtrades.query.order_by(desc(Ethtrades.time_recorded)).limit(30).all()
    rows_xrpusd = Xrptrades.query.order_by(desc(Xrptrades.time_recorded)).limit(30).all()

    rows_btc=[]
    rows_eth=[]
    rows_xrp=[]

    for item in rows_btcusd:
        rows_btc.append(item.as_dict())
    for item in rows_ethusd:
        rows_eth.append(item.as_dict())
    for item in rows_xrpusd:
        rows_xrp.append(item.as_dict())


    return render_template('trades.html', rows_btc=rows_btc, rows_eth=rows_eth, rows_xrp=rows_xrp)

#logout route - redirect to landing page
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
