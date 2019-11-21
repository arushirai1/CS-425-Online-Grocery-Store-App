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
    user_id = db.Column(db.Integer, primary_key=True)
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
    customer_ID = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
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




class customer_address(db.Model):

    __tablename__='customer_address'

    customer_ID =db.Column(db.Integer, db.ForeignKey(Customer.customer_ID), primary_key=True)
    street_address=db.Column(db.String())
    city=db.Column(db.String())
    state=db.Column(db.String())
    zip_code=db.Column(db.Integer)

    def __init__ (self,customer_ID, street_address,city,zip_code):
        self.customer_ID=customer_ID
        self.street_address=street_address
        self.city=city
        self.zip_code=zip_code

    def __repr__(self):
        return '<id {}>'.format(self.customer_ID)

    def serialize(self):
        return{
            'customer_ID': self.customer_ID,
            'street_address': self.street_address,
            'city': self.city,
            'zip_code': self.zip_code,
        }

class credit_card(db.Model):

    __tablename__='credit_card'

    customer_ID =db.Column(db.Integer,db.ForeignKey(Customer.customer_ID), primary_key=True)
    card_number=db.Column(db.Integer, primary_key=True)
    street_address=db.Column(db.String())
    city=dp.Column(db.String())
    state=db.Column(db.String())
    zip_code=db.Column(db.Integer)
    
    def __init__ (self,customer_ID,card_number,street_address,city,zip_code):
        self.customer_ID=customer_ID
        self.card_number=card_number
        self.street_address=street_address
        self.city=city
        self.zip_code=zip_code

    def __repr__(self):
        return '<id {}>'.format(self.customer_ID)

    def serialize(self):
        return{
            'customer_ID': self.customer_ID,
            'card_number': self.card_number,
            'street_address': self.street_address,
            'city': self.city,
            'zip_code': self.zip_code,
        }


class pricing(db.Model):

    __tablename__='pricing'

    product_ID =db.Column(db.Integer, db.ForeignKey(Customer.customer_ID),primary_key=True)
    state=db.Column(db.String())
    price=db.Column(db.Double)
    
    def __init__ (self,customer_ID,card_number,street_address,city,zip_code):
        self.customer_ID=customer_ID
        self.card_number=card_number
        self.street_address=street_address
        self.city=city
        self.zip_code=zip_code

    def __repr__(self):
        return '<id {}>'.format(self.customer_ID)

    def serialize(self):
        return{
            'customer_ID': self.customer_ID,
            'card_number': self.card_number,
            'street_address': self.street_address,
            'city': self.city,
            'zip_code': self.zip_code,
        }




