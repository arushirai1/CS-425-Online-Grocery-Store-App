from app import db
from sqlalchemy.dialects.postgresql import JSON

class Test(db.Model):
    __tablename__ = 'test'

    test_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    name2 = db.Column(db.String())
    age = db.Column(db.Integer)
    def __init__(self, name, name2, age):
        self.name = name
        self.name2 = name2
        self.age = age

    def __repr__(self):
        return '<id {}>'.format(self.test_id)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'test_id': self.test_id, 
            'name': self.name,
            'name2': self.name2,
        }

class Users(db.Model):
    __tablename__ = 'users'
    user_id	= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User id {}>'.format(self.user_id)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'user_id': self.user_id, 
            'username': self.username,
            'password': self.password,
        }

class Customer(db.Model):
    __tablename__ = 'customer'
    customer_ID	= db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    name = db.Column(db.String())
    balance = db.Column(db.Integer)

    def __init__(self, customer_ID, name, balance):
        self.customer_ID = customer_ID
        self.name = name
        self.balance = balance

    def __repr__(self):
        return '<Customer id {}>'.format(self.customer_ID)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'customer_ID': self.customer_ID, 
            'name': self.name,
            'balance': self.balance,
        }

