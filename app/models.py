from . import db
from flask_login import UserMixin
from uuid import uuid4 #for generating primary keys

#Table for storing basic user details once they register
class User(UserMixin,db.Model):
    id = db.Column(db.String,default=lambda: str(uuid4().hex), primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(120))
    firstname = db.Column(db.String(20), unique=False)
    lastname = db.Column(db.String(20), unique=False)
    create_date = db.Column(db.DateTime, unique=False)

    #This is a custom deserializer for complex objects when needed
    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

#table for btc trades
class Btctrades(db.Model):
    id = db.Column(db.String,default=lambda: str(uuid4().hex), primary_key=True)
    channel_id = db.Column(db.Integer, unique=False)
    msg_type = db.Column(db.String(5), unique=False)
    trade_id = db.Column(db.String(20), unique=True)
    timestamp = db.Column(db.Integer)
    price = db.Column(db.Float, unique=False)
    amount = db.Column(db.Float, unique=False)
    time_recorded = db.Column(db.DateTime, unique=False)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


#table for eth trades
class Ethtrades(db.Model):
    id = db.Column(db.String,default=lambda: str(uuid4().hex), primary_key=True)
    channel_id = db.Column(db.Integer, unique=False)
    msg_type = db.Column(db.String(5), unique=False)
    trade_id = db.Column(db.String(20), unique=True)
    timestamp = db.Column(db.Integer)
    price = db.Column(db.Float, unique=False)
    amount = db.Column(db.Float, unique=False)
    time_recorded = db.Column(db.DateTime, unique=False)


    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

#table for xrp trades
class Xrptrades(db.Model):
    id = db.Column(db.String,default=lambda: str(uuid4().hex), primary_key=True)
    channel_id = db.Column(db.Integer, unique=False)
    msg_type = db.Column(db.String(5), unique=False)
    trade_id = db.Column(db.String(20), unique=True)
    timestamp = db.Column(db.Integer)
    price = db.Column(db.Float, unique=False)
    amount = db.Column(db.Float, unique=False)
    time_recorded = db.Column(db.DateTime, unique=False)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
