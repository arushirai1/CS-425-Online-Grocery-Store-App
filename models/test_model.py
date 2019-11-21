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

class Staff(db.Model):
    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    name = db.Column(db.String())
    title = db.Column(db.String())
    salary = db.Column(db.Integer)
    address_line1 = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip_code = db.Column(db.Integer)

    def __init__(self, staff_id, name, title, salary, address_line1, city, state, zip_code):
        self.staff_id = staff_id
        self.name = name
        self.title = title
        self.salary = salary
        self.address_line1 = address_line1
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return '<Staff id {}>'.format(self.staff_id)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'staff_id': self.staff_id, 
            'name': self.name,
            'title': self.title,
            'salary': self.salary,
            'balance': self.balance,
            'address_line1': self.address_line1, 
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code
        }

class Product(db.Model):
    __tablename__ = 'product'

    product_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    product_type = db.Column(db.String())
    size = db.Column(db.Numeric)
    alcohol_content = db.Column(db.Numeric)
    nutritional_value = db.Column(db.Integer)

    def __init__(self, product_ID, name, product_type, size, alcohol_content, nutritional_value):
        self.product_ID = product_ID
        self.name = name
        self.product_type = product_type
        self.size = size
        self.alcohol_content = alcohol_content
        self.nutritional_value = nutritional_value

    def __repr__(self):
        return '<Product id {}>'.format(self.product_ID)
    
    #used for JSON formatting    
    def serialize(self):
        return {
            'product_ID': self.product_ID, 
            'name': self.name,
            'product_type': self.product_type,
            'size': self.size,
            'alcohol_content': self.alcohol_content,
            'nutritional_value': self.nutritional_value
        }


